from django.db import models

# Create your models here.

class UserInfo(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=16, verbose_name='密码')

    def __str__(self):
        return self.name