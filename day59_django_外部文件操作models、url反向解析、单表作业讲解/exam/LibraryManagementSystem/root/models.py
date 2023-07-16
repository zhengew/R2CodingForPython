from django.db import models
from decimal import Decimal

"""
books 表
"""

class Book(models.Model):

    id = models.AutoField(primary_key = True, verbose_name='book表id')
    bname = models.CharField(max_length=50, unique=True, default='', verbose_name='书籍名称')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')
    publishDate = models.DateField(verbose_name='出版日期')
    publisher = models.CharField(max_length=50, null=False, verbose_name='出版社')

    def __str__(self):
        return self.bname


class UserInfo(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='用户id')
    username = models.CharField(max_length=16, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, null=False, default='123456', verbose_name='密码')

    def __str__(self):
        return self.username