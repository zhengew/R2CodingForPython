from django.contrib import admin

# Register your models here.
from appRoot import models
# 用户表
admin.site.register(models.UserInfo)