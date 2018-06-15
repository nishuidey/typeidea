from __future__ import unicode_literals


from django.db import models

from blogs.models. import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="文章")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CHarField(max_lenght=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"