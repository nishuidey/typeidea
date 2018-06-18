from __future__ import unicode_literals

from pprint import pprint as pp

from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase
from django.test.utils import override_settings
from django.db.models import Q, F

from .models import Category, Post


class TestCategory(TestCase):
    def setUp(self):
        self.user = user = User.objects.create_user('nishuideyu', '1@1qq.com', 'password')
        # for i in range(10):
        #     category_name = 'cate_%s' % i
        #     Category.objects.create(name=category_name, owner=user)
        Category.objects.bulk_create([
            Category(name='cate_bulk_%s' % i, owner=user)
            for i in range(10)
        ])
        pp(connection.queries)
        print('-' * 10)

    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.filter(
            (Q(id=1) | Q(id=2))
        )
        print(categories)

        print('===' * 10)
        category = Category.objects.filter(id=1).update(status=F('status') + 1)
        users = User.objects.filter(username='nishuideyu').annotate(cate_count=Count('category'))
        user = users[0]
        print(user.cate_count)
        pp(connection.queries)

