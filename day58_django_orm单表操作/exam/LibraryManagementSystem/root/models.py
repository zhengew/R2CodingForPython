from django.db import models
from decimal import Decimal

"""
books 表
"""

class Book(models.Model):

    id = models.AutoField('book表id', primary_key = True)
    bname = models.CharField('书籍名称', max_length=50, unique=True)
    price = models.DecimalField('价格', max_digits=8, decimal_places=2)
    publishDate = models.DateField('出版日期')
    publisher = models.CharField('出版社', max_length=50, null=False)

    def __str__(self):
        return self.bname


class UserInfo(models.Model):

    id = models.AutoField('用户id', primary_key=True)
    username = models.CharField('用户名', max_length=16, unique=True)
    password = models.CharField('密码', max_length=32, null=False, default='123456')