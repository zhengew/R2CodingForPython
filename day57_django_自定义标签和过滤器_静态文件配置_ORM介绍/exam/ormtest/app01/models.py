from django.db import models

# Create your models here.

class UserInfo(models.Model):

    id = models.AutoField(primary_key=True)
    # create table UserInfo (id int primary key auto_increment, name varchar(16), age int, current_date date);

    name = models.CharField(max_length=16)

    age = models.IntegerField()

    current_date = models.DateField()

