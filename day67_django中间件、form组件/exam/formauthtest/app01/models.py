import uuid

from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):

    # id = models.AutoField(primary_key=True, verbose_name='用户id')
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, verbose_name='uuid')
    username = models.CharField(max_length=16, unique=True, null=False, blank=False, verbose_name='用户名')
    password = models.CharField(max_length=32, null=False, blank=False, verbose_name='密码')

    def __str__(self):
        return self.username


# 作者详细信息表
class AuthorDetail(models.Model):

    # id = models.AutoField(primary_key=True, verbose_name='作者详情id')
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, verbose_name='uuid')
    birthday = models.DateField(verbose_name='出生日期')
    telphone = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=50, verbose_name='办公地址')

    def __str__(self):
        return self.address

# 性别
class Gender(models.TextChoices):

    MAN = '1', 'man'
    FEMAN = '2', 'feman'


# 作者表
class Author(models.Model):

    # GENDER_CHOICES = [('1', 'man'), ('2', 'feman'),]

    # id = models.AutoField(primary_key=True, verbose_name='作者表id')
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, verbose_name='uuid')
    name = models.CharField(max_length=16, null=False, blank=False,  verbose_name='姓名')
    sex = models.CharField(
            max_length=1,
            choices=Gender.choices,
            default=Gender.MAN,
    )
    author_detail = models.OneToOneField(to='AuthorDetail', to_field='id', on_delete=models.CASCADE, verbose_name='外键，作者详情表id, 一对一关系')

    def __str__(self):

        return self.name

# 出版社表
class Publish(models.Model):

    # id = models.AutoField(primary_key=True, verbose_name='出版社表id')
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, verbose_name='uuid')
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='出版社名称')
    city = models.CharField(max_length=50, null=False, blank=False, verbose_name='出版社注册地址')
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='邮箱')

    def __str__(self):

        return self.name

# 书籍表
class Book(models.Model):

    # id = models.AutoField(primary_key=True, verbose_name='书籍表ID')
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, verbose_name='uuid')
    bname = models.CharField(max_length=50, null=False, blank=False, verbose_name='书籍名称')
    publish_date = models.DateField(null=False, blank=False, verbose_name='出版日期')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    publishs = models.ForeignKey(to='Publish', to_field='id', on_delete=models.CASCADE, verbose_name='外键，出版社表id') # TODO 多对一
    authors = models.ManyToManyField(to='Author', verbose_name='中间表') # TODO 多对多

    def __str__(self):

        return self.bname

    # 查询书籍作者
    def get_all_authors(self):

        return ','.join([author.name for author in self.authors.all()])


