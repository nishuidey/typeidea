# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category
from typeidea.config.models import SideBar
from typeidea.comment.models import Comment
from typeidea.comment.forms import CommentForm


class CommonMixin(object):
    def get_category_context(self):
        categories = Category.objects.filter(status=1)  # TODO: fix magic number

        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)
        return {
            'nav_cates': nav_cates,
            'cates': cates,
        }

    def get_context_data(self, **kwargs):
        side_bars = SideBar.objects.filter(status=1)

        recently_posts = Post.objects.filter(status=1)[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]
        kwargs.update({
            'side_bars': side_bars,
            'recently_comments': recently_comments,
            'recently_posts': recently_posts,
        })
        kwargs.update(self.get_context_data())
        return super(CommonMixin, self).get_context_data(**kwargs)


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasePostView):
    pass


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []

        posts = tag.posts.all()
        return posts


class AuthorView(BasePostView):
    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        qs = super(AuthorView, self).get_queryset()
        if author_id:
            qs = qs.filter(owner_id=author_id)
        return qs


class PostView(CommonMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_comments(self):
        target = self.request.path
        comments = Comment.object.filter(target=target)
        return comments

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
            'comments': self.get_comments(),
        })
        return super(PostView, self).get_context_data(**kwargs)
