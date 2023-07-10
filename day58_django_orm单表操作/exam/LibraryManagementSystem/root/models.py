from enum import unique

from django.db import models

# Create your models here.

class Books(models.Model):

    def __str__(self):
        return self.bname

    id = models.AutoField(primary_key=True),
    bname = models.CharField(max_length=50, null=True),
    # price = models.FloatField(null=False),
    # publication_date = models.DateTimeField(auto_now_add=True),
    # publisher = models.CharField(max_length=50, null=False),

class Book(models.Model):

    def __str__(self):
        return self.bname

    id = models.AutoField(primary_key=True),
    bname = models.CharField(max_length=50, null=True),

