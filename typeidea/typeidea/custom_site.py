# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 7:09
# @Author  : nishuideyu

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
