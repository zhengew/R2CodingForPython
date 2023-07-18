from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='id')
    username = models.CharField(max_length=16, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')

    def __str__(self):
        return self.username

# 作者表
class Author(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=16, unique=True, verbose_name='姓名')
    sex = models.CharField(max_length=1, choices=[('1', 'male'), ('2', 'female')], default='1', verbose_name='性别, 1-male, 2-female, 默认 1')
    authorDetail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE, verbose_name='作者详细表id, 外键')

    def __str__(self):
        return self.name


# 作者详细信息表
class AuthorDetail(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='id')
    birthday = models.DateField(verbose_name='生日')
    mobile = models.CharField(max_length=32, verbose_name='电话')
    address = models.CharField(max_length=50, verbose_name='地址')

    def __str__(self):
        return self.address

# 出版社表
class Publish(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=16, verbose_name='出版社名称')
    city = models.CharField(max_length=16, verbose_name='出版社办公地址')
    email = models.EmailField(max_length=50, verbose_name='邮箱')

    def __str__(self):
        return self.name

# 书籍表
class Book(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='id')
    bname = models.CharField(max_length=16, verbose_name='书籍名称')
    publishDate = models.DateField(verbose_name='出版日期')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='价格')
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE, verbose_name='出版社id, 外键')
    author = models.ManyToManyField(to='Author', verbose_name='作者id, 外键')

    def __str__(self):
        return self.bname