# Generated by Django 4.2.2 on 2023-07-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='book表id')),
                ('bname', models.CharField(default='', max_length=50, unique=True, verbose_name='书籍名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('publishDate', models.DateField(verbose_name='出版日期')),
                ('publisher', models.CharField(max_length=50, verbose_name='出版社')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('username', models.CharField(max_length=16, unique=True, verbose_name='用户名')),
                ('password', models.CharField(default='123456', max_length=32, verbose_name='密码')),
            ],
        ),
    ]
