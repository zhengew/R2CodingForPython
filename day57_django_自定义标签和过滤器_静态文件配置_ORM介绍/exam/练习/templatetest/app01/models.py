from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=16, null=True, blank=True, db_index=True)

    sex = models.IntegerField(default=1, unique=True, choices=((1, '男'), (2, '女'), (3, '二椅子')))

    current_date = models.DateField(auto_now=True)