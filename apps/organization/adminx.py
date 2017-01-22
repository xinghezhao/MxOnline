# -*- coding: utf-8 -*-
__author__ = 'xinghezhao'
__date__ = '17-1-1 下午11:56'


import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):


    list_display = ['name', 'desc', 'add_time'] #显示字段
    search_fields = ['name', 'desc' ]  #搜索功能
    list_filter = ['name', 'desc', 'add_time'] #过滤器


class CourseOrgAdmin(object):

    list_display = ['name', 'desc','click_nums', 'fav_nums'] #显示字段
    search_fields = ['name', 'desc','click_nums']  #搜索功能
    list_filter = ['name', 'desc','click_nums', 'fav_nums'] #过滤器

    # relfield_style = 'fk-ajax' #当某个外键指向它可以设置(改为搜索功能)


class TeacherAdmin(object):

    list_display = ['org', 'name','work_years', 'work_company'] #显示字段
    search_fields = ['org', 'name','work_years', 'work_company']  #搜索功能
    list_filter = ['org', 'name','work_years', 'work_company'] #过滤器


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

