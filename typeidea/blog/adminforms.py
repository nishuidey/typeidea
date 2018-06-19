# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 14:11
# @Author  : nishuideyu

from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label="摘要", required=False)
