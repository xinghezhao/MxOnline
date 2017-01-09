# -*- coding: utf-8 -*-
__author__ = 'xinghezhao'
__date__ = '17-1-1 下午11:39'

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']  # 显示字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                     'click_nums']  # 搜索功能
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']  # 过滤器


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']  # 显示字段
    search_fields = ['course', 'name']  # 搜索功能
    list_filter = ['course__name', 'name', 'add_time']  # 过滤器


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']  # 显示字段
    search_fields = ['lesson', 'name']  # 搜索功能
    list_filter = ['lesson', 'name', 'add_time']  # 过滤器


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']  # 显示字段
    search_fields = ['course', 'name', 'download']  # 搜索功能
    list_filter = ['course', 'name', 'download', 'add_time']  # 过滤器


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)