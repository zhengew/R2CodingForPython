from django.contrib import admin
from root import models
# Register your models here.

# 用户表
admin.site.register(models.UserInfo)
# 出版社表
admin.site.register(models.Publish)
# 作者详细信息表
admin.site.register(models.AuthorDetail)
# 作者表
admin.site.register(models.Author)
# 书籍表
admin.site.register(models.Book)