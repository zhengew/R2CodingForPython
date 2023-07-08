from django.db import models

class UserInfo(models.Model): # 继承 models模块的Model类

    id = models.AutoField(primary_key = True) # id int primary key auto_increment

    name = models.CharField(max_length=16, null=False)

    age = models.IntegerField(null = False)

    sex = models.IntegerField(default=1, unique=True, choices=((1, '男'), (2, '女'), (3, '不详')))

    birth = models.DateField(null=False)
