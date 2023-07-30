from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):

    id = models.AutoField(primary_key = True, verbose_name = '主键id')
    username = models.CharField(max_length=16, unique=True, verbose_name='姓名')
    password = models.CharField(max_length=32, verbose_name='密码')

    def __str__(self):
        return self.username

# 作者详细信息表
class AuthorDetail(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    birthday = models.DateField(verbose_name='出生日期')
    mobile = models.CharField(max_length=16, verbose_name='电话')
    address = models.CharField(max_length=50, verbose_name='地址')

    def __str__(self):

        return self.address

# 作者表
class Author(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    name = models.CharField(max_length=16, verbose_name='姓名')
    sex = models.CharField(max_length=1, choices=[('1', 'male'), ('2', 'female')], default='1')
    authorDetail = models.OneToOneField(to='AuthorDetail', to_field='id', on_delete=models.CASCADE, verbose_name='外键')

    def __str__(self):

        return self.name

# 出版社表
class Publish(models.Model):

    id = models.AutoField(primary_key=True, verbose_name = '主键id')
    name = models.CharField(max_length=50, unique=True, null=True, verbose_name='出版社')
    city = models.CharField(max_length=50, verbose_name='城市')
    email = models.CharField(max_length=50, verbose_name='邮箱')

    def __str__(self):

        return self.name

# 书籍表
class Book(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='主键id')
    bname = models.CharField(max_length=50, verbose_name='书籍名称')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    good = models.IntegerField(default=1, verbose_name='点赞')
    comment = models.IntegerField(default=1, verbose_name='评论')
    publishDate = models.DateField(verbose_name='出版日期')
    publishs = models.ForeignKey(to='Publish', to_field='id', on_delete=models.CASCADE, verbose_name='外键,出版社id', ) # related_name='Publish' 别名，替换反向查询的小写表名
    authors = models.ManyToManyField(to='Author', verbose_name='中间表, root_book_authors')

    def __str__(self):

        return self.bname