from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='用户id')
    username = models.CharField(max_length=16, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')

    def __str__(self):
        return self.username