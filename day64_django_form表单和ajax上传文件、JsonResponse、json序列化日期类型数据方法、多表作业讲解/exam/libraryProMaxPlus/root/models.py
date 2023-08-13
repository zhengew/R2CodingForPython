from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='用户id')
    username = models.CharField(max_length=16, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')

    def __str__(self):
        return self.username

# 出版社表
class Publish(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='出版社id')
    name = models.CharField(max_length=48, unique=True, verbose_name='出版社名称')
    city = models.CharField(max_length=48, null=False, verbose_name='注册地')
    email = models.CharField(max_length=48, null=False, verbose_name='邮箱')

    def __str__(self):
        return self.name

# 作者详细信息表
class AuthorDetail(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='作者详细信息表id')
    birthday = models.DateField(verbose_name='出生日期')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    address = models.CharField(max_length=100, verbose_name='住址')

    def __str__(self):
        return self.address

# 作者表
class Author(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='作者表id')
    name = models.CharField(max_length=16, unique=True, verbose_name='姓名')
    sex = models.CharField(max_length=6, default='male', verbose_name='性别')
    authorDetail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE, verbose_name='外键') # TODO: 一对一关系

    def __str__(self):
        return self.name

# 书籍表
class Book(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='书籍表id')
    bname = models.CharField(max_length=16, null=False, verbose_name='书名')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    publishDate = models.DateField(null=False, verbose_name='出版日期')
    publishs = models.ForeignKey(to='Publish', on_delete=models.CASCADE, verbose_name='外键') # TODO: 一对多
    authors = models.ManyToManyField(to='Author', verbose_name='中间表') # TODO: 多对多

    def __str__(self):
        return self.bname