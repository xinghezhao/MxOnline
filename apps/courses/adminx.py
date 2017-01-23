# -*- coding: utf-8 -*-
__author__ = 'xinghezhao'
__date__ = '17-1-1 下午11:39'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg

class LessonInline(object):
    model = Lesson  #实现在课程资源添加的同时添加章节
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums',
                    'add_time','get_zj_nums','go_to']  # 显示字段
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums',
                     'click_nums']  # 搜索功能
    list_filter = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums',
                   'add_time']  # 过滤器

    ordering = ['-click_nums'] #设置排序
    readonly_fields = ['click_nums']#设置为只读（不可编辑）
    list_editable = ['degree', 'desc'] #在课程列表页进行编辑
    exclude = ['fav_nums'] #设置隐藏 exclude和readonly_fields 设置字段冲突
    inlines = [LessonInline,CourseResourceInline]
    refresh_times = [3, 5]#定时刷新列表页
    style_fields = {"detail":"ueditor"}
    import_excel = True  #设置导入excel表


    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        #在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)




class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']  # 显示字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                     'click_nums']  # 搜索功能
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']  # 过滤器

    ordering = ['-click_nums'] #设置排序
    readonly_fields = ['click_nums']#设置为只读（不可编辑）
    exclude = ['fav_nums'] #设置隐藏 exclude和readonly_fields 设置字段冲突
    inlines = [LessonInline,CourseResourceInline]


    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return  qs




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
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)