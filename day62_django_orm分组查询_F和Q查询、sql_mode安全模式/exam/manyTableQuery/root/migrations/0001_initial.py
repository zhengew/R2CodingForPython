# Generated by Django 4.2.2 on 2023-07-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('username', models.CharField(max_length=16, unique=True, verbose_name='姓名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
    ]
