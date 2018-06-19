# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag
from django.urls import reverse
from django.utils.html import format_html
from typeidea.custom_site import custom_site


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'show_status', 'owner', 'created_time', 'operator']
    list_filter = ['category']
    save_on_top = True
    search_fields = ['title', 'category__name', 'owner__username']

    actions_on_top = True
    actions_on_bottom = False
    date_hierarchy = 'created_time'

    fieldsets = (
        ('基础配置', {
            'fields': (('category', 'title'), 'content')
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),
            'fields': ('tags',),
        }),
    )
    filter_horizontal = ('tags',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass




