# _*_ coding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView  #用于(网页首页)显示静态文件
import xadmin
from django.views.static import serve  #用于处理上传静态文件

from users.views import LogoutView, LoginView, RegisterView, ActiveUserView,ForgetPwdView, ResetView, ModifyPwdView
from users.views import IndexView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT #,STATIC_ROOT  #(当debug改为true时需要增加)



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # url(r'^$', IndexView.as_view(template_name='index.html'), name='index'),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$',LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$',RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),   #提取变量 用于用户激活
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),   #找回密码
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    #课程机构相关URL配置
    url(r'^org/', include('organization.urls', namespace='org')),


    #课程相关URL配置
    url(r'^course/', include('courses.urls', namespace='course')),

    # 个人中心相关URL配置
    url(r'^users/', include('users.urls', namespace='users')),

    # 配置上传文件的访问函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),


    #配置static的访问函数
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    #富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]

#全局404页面配置
handler404 = 'users.views.page_not_fond'

#全局500页面配置
handler500 = 'users.views.page_error'




