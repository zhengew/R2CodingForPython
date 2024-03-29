# Generated by Django 4.2.2 on 2023-07-17 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_authordetail_alter_userinfo_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=16, verbose_name='出版社名称')),
                ('city', models.CharField(max_length=16, verbose_name='出版社办公地址')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
            ],
        ),
        migrations.AlterField(
            model_name='authordetail',
            name='address',
            field=models.CharField(max_length=50, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='authordetail',
            name='mobile',
            field=models.CharField(max_length=32, verbose_name='电话'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('bname', models.CharField(max_length=16, verbose_name='书籍名称')),
                ('publishDate', models.DateField(verbose_name='出版日期')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='价格')),
                ('author', models.ManyToManyField(to='root.author', verbose_name='作者id, 外键')),
                ('publish_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.publish', verbose_name='出版社id, 外键')),
            ],
        ),
    ]
