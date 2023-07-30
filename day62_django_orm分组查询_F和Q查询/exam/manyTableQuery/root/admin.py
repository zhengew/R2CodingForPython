from django.contrib import admin
from root import models
# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.AuthorDetail)
admin.site.register(models.Author)
admin.site.register(models.Publish)
admin.site.register(models.Book)

