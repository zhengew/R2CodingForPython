from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.

def index(request):

    # 创建记录方式一
    # student_obj = models.Student(
    #     name = 'dazhuang',
    #     age = 23,
    # )
    # student_obj.save() # 保存

    # 创建记录方式二
    # new_obj = models.Student.objects.create(name='xiaozhuang', age=5) # objects控制器 调用 create方法
    # print(new_obj) # Student object ---- model对象
    # print(new_obj.name)
    # print(new_obj.age)

    # 创建方式三： 批量创建
    # objs_list = []
    # for i in range(100, 3000000):
    #     obj = models.Student(
    #         name = 'xiangxixxx',
    #         age = 10,
    #     )
    #     objs_list.append(obj)
    #
    # models.Student.objects.bulk_create(objs_list)


    # 创建方法四： update_or_create 有就更新没有就创建
    models.Student.objects.update_or_create(
        name = '雪飞2',
        defaults={
            'age': 48,
        }
    )


    # 简单查询
    # 查询所有数据：all方法
    # <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>,
        # <Student: Student object (3)>, <Student: Student object (4)>]>  -- 类似于列表  -- QuerySet 集合
    # all_objs = models.Student.objects.all()
    # print(all_objs)

    # for i in all_objs:
    #     print(i.name)


    # 条件查询： .filter 方法, 返回的也是 QuerySet 集合, 查询不到不会报错，返回一个空的 QuerySet
    # objs = models.Student.objects.filter(id=2) #  查询 id = 2 的那条记录
    # print(objs)
    # objs = models.Student.objects.filter(name='dazhuang')
    # print(objs)

    # 条件查询： .get方法, 返回的是 model对象，而且get方法有且只有一个结果
    # 报错1：数据查询结果大于1条: get() returned more than one Student -- it returned 3!
    # 报错2: 没有查到任何内容: Student matching query does not exist.
    # obj = models.Student.objects.get(id='1')
    # print(obj)


    # 删除 delete, QuerySet 和 model对象都可以调用
    # models.Student.objects.get(id=3).delete()  # model对象调用 delete方法
    # models.Student.objects.filter(name='dazhuang').delete() # QuerySet调用 delete 方法

    # 删除所有
    # models.Student.objects.all().delete()


    # 更新 update, model对象不能调用 update方法, 只能 QuerySet调用
    ### app01.models.Student.DoesNotExist: Student matching query does not exist.
    ### models.Student.objects.get(name='雪飞').update(age=38)

    # models.Student.objects.filter(name='雪飞').update(age=38) # QuerySet 调用 delete方法


    # 查询接口2

    # 1. 多条件查询
    # models.Student.objects.filter(id=8, name='大壮').update(
    #     name='大壮禅师',
    #     age = 78
    # )
    # 打散形式传参数
    models.Student.objects.filter(**{'id': 8, 'name': '大壮禅师'}).update( # **： 函数使用时表示打散
        age = 100
    )

    return render(request, 'index.html')

