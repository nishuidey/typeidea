# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 15:20
# @Author  : nishuideyu

from __future__ import unicode_literals

from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1.用来处理文章、分类、标签、侧边栏、友链这些model的owner字段
    2.用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner',)
    
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

