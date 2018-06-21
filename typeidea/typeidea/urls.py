# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import path, re_path, include

from typeidea.blog.views import IndexView, CategoryView, TagView, PostView, AuthorView
from .custom_site import custom_site

from typeidea.comment.views import CommentView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name='category'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    re_path(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='detail'),
    re_path(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    path('comment', CommentView.as_view(), name='comment'),
    path('admin', admin.site.urls),
    path('cus_admin', custom_site),
]
