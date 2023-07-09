from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=16)
    age = models.IntegerField(default=1)
    # age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
