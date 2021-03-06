from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '可用'),
        (2, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "分类"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "标签"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (3, '删除'),
    )
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    content = models.TextField(verbose_name="内容", help_text="注：目前仅支持Markdown格式数据")
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def show_status(self):
        return '当前状态:%s' % self.status
    show_status.short_description = '展示状态'

    class Meta:
        verbose_name = verbose_name_plural = "文章"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class TestManager(models.Manager):
    def get_queryset(self):
        return super(TestManager, self).get_queryset().filter(status=1)


    


