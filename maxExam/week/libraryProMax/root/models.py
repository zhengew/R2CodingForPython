from enum import unique

from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    username = models.CharField(max_length=16, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, unique=True, verbose_name='密码')

    def __str__(self):
        return self.username

# 出版社表
class Publish(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    name = models.CharField(max_length=50, verbose_name='出版社名称')
    city = models.CharField(max_length=50, verbose_name='城市')
    email = models.EmailField(max_length=50, verbose_name='邮箱')

    def __str__(self):

        return self.name

# 作者详细信息表
class AuthorDetails(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    birthday = models.DateField(verbose_name='出生日期')
    telphone = models.CharField(max_length=20, verbose_name='电话')
    address = models.CharField(max_length=50, verbose_name='地址')

    def __str__(self):

        return self.address

# 作者表
class Author(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    name = models.CharField(max_length=21, verbose_name='姓名')
    sex = models.CharField(max_length=6, default='male', verbose_name='性别,默认male')
    authorDetails = models.OneToOneField(to='AuthorDetails', to_field='id', on_delete=models.CASCADE, verbose_name='外键') # TODO: 一对一

    def __str__(self):

        return self.name

# 书籍表
class Book(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    title = models.CharField(max_length=50, verbose_name='书名')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    publishDate = models.DateField(verbose_name='出版日期')
    publishs = models.ForeignKey(to='Publish', to_field='id', on_delete=models.CASCADE, verbose_name='外键') # TODO: 一对多
    authors = models.ManyToManyField(to='Author', verbose_name='中间表, root_book_authors')

    def __str__(self):

        return self.title