# _*_ coding:utf-8 _*_
import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend #通过邮箱登陆
from django.db.models import Q #Q表示或
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password #把明文密码加密
from django.http import HttpResponse, HttpResponseRedirect  #HttpResponseRedirect重定View

from .models import UserProfile,EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm, UploadImageForm
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin #用户登陆

#通过类实现邮箱登陆
class CustomBackend(ModelBackend):  #通过邮箱登陆
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class RegisterView(View):  #注册
    def get(self,request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email','')
            if UserProfile.objects.filter(email = user_name):    #判断用户是否存在
                return render(request, 'register.html', {'register_form':register_form, 'msg': '用户已经存在'})


            pass_word = request.POST.get('password','')
            user_profile =UserProfile()
            user_profile.username =user_name
            user_profile.email =user_name
            user_profile.is_active = False  #数据库中is_active 默认是False 没有激活,当变为True时为激活
            user_profile.password = make_password(pass_word)   #密码加密
            user_profile.save()

            send_register_email(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form':register_form})


#通过类实现退出

class LogoutView(View):
    """
    用户登录
    """
    def get(self, request):
        logout(request)
        from django.core.urlresolvers import reverse #
        return HttpResponseRedirect(reverse('index'))





#通过类实现登陆
class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户未激活!'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误!'})
        else:
            return render(request, 'login.html',{'login_form':login_form})


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html',{'forget_form':forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html',{'email':email})

        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyPwdView(View):
    """
    修改用户密码
    """
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg':'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)  # 密码加密
            user.save()

            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email': email, 'modify_form': modify_form})



class UserinfoView(LoginRequiredMixin,View):
    """
    用户个人信息
    """
    def get(self,request):
        return  render(request, 'usercenter-info.html',{})


class UploadImageView(LoginRequiredMixin, View):
    """
    用户修改头像
    """
    def post(self,request):
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')



class UpdatePwdView(View):
    """
    个人中心修改用户密码
    """
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type='application/json')
            user = request.user
            user.password = make_password(pwd2)  # 密码加密
            user.save()

            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')



class SendEmailCodeView(LoginRequiredMixin, View):
    """
    发送邮箱验证码
    """
    def get(self, request):
        email = request.GET.get('email','')

        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已经存在"}', content_type='application/json')
        send_register_email(email, 'update_email')

        return HttpResponse('{"status":"sucess"}', content_type='application/json')


class UpdateEmailView(LoginRequiredMixin, View):
    """
    修改个人邮箱
    """

    def post(self, request):
        pass




# Create your views here.




