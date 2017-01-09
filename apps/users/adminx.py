# -*- coding: utf-8 -*-
__author__ = 'xinghezhao'
__date__ = '17-1-1 下午10:58'

import xadmin

from .models import EmailVerifyRecord,Banner

class EmailVerifyRecordAdmin(object):

    list_display = ['code','email','send_type','send_time']  #后台自定义显示列
    search_fields = ['code','email','send_type'] #定义后台搜索
    list_filter = ['code','email','send_type','send_time'] #通过时间搜索


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time'] #后台自定义显示列 显示字段
    search_fields = ['title', 'image', 'url', 'index'] #定义后台搜索 搜索功能
    list_filter = ['title', 'image', 'url', 'index', 'add_time'] #过滤器 通过时间搜索

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)

