# -*- coding: utf-8 -*-
__author__ = 'xinghezhao'
__date__ = '17-1-1 下午10:58'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import EmailVerifyRecord,Banner,UserProfile



class UserProfileAdmin(UserAdmin):
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


class EmailVerifyRecordAdmin(object):

    list_display = ['code','email','send_type','send_time']  #后台自定义显示列
    search_fields = ['code','email','send_type'] #定义后台搜索
    list_filter = ['code','email','send_type','send_time'] #通过时间搜索
    model_icon = 'fa fa-envelope'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time'] #后台自定义显示列 显示字段
    search_fields = ['title', 'image', 'url', 'index'] #定义后台搜索 搜索功能
    list_filter = ['title', 'image', 'url', 'index', 'add_time'] #过滤器 通过时间搜索




#from django.contrib.auth.models import User
#xadmin.site.unregister(User)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
#xadmin.site.register(UserProfile, UserProfileAdmin)


# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSettings)



