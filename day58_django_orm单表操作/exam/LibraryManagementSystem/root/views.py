from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from root import models

class Library(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):

        """新增"""
        # 1.方式一：
        # user_Obj = models.UserInfo(
        #     username = 'test1',
        #     password = '123456',
        # )
        # user_Obj.save()

        # 2.方式二
        # obj = models.UserInfo.objects.create(
        #     username = 'test2',
        #     password = '123456',
        # )
        #
        # print(obj) # UserInfo object (3) -- 返回值是model对象
        # print(obj.username, obj.password) # test2 123456

        # 3. 方式三：批量创建
        # user_obj_list = []
        # for i in range(3, 11):
        #     obj = models.UserInfo(
        #         username = 'test%s' % i,
        #         password = '123456',
        #     )
        #     user_obj_list.append(obj)
        # models.UserInfo.objects.bulk_create(user_obj_list)

        # books_list = []
        # for i in range(1, 21):
        #     obj = models.Book(**{'bname': 'book%s' % i, 'price': 100 + i, 'publishDate': '2018-01-%s' % i,
        #                          'publisher': '人民邮电出版社'}, )
        #     books_list.append(obj)
        #
        # models.Book.objects.bulk_create(books_list)


        # 4. 方式四： update_or_create 有就更新，没有就新增
        # models.UserInfo.objects.update_or_create(
        #     username='alex',
        #     defaults = {
        #         'password': '123456',
        #     }
        # )

        # 5.添加日期类型数据
        ## 5.1 方式一： 实例化时间对象作为date属性的value
        # import datetime
        # curr_date = datetime.datetime.now() # 当前时间
        # models.Book.objects.create(
        #     **{
        #         'bname': 'Python Cookbook',
        #         'price': 108.00,
        #         'publishDate': curr_date,
        #         'publisher': '人民邮电出版社'
        #     }
        # )

        ## 5.2 方式二 使用日期字符串
        # models.Book.objects.create(
        #     **{
        #         'bname': '流畅的Python',
        #         'price': 139.00,
        #         'publishDate': '2017-05-15',
        #         'publisher': '人民邮电出版社'
        #     }
        # )



        # models.Book.objects.create(
        #     bname = '天才在左，疯子在右',
        #     price= 49.80,
        #     publishDate =  '2018-05-01',
        #     publisher = '北京联合出版公司',
        #
        # )
        #
        # models.Book.objects.create(
        #     bname = '计算机组成原理',
        #     price =  56.90,
        #     publishDate =  '2017-03-15',
        #     publisher = '机械工业出版社',
        #
        # )

        """删除"""
        # 1.model对象调用 delete方法
        # models.Book.objects.get(id=1).delete()  # get 方法返回的时 model对象
        # 2.QuerySet调用 delete方法
        # models.Book.objects.filter(id=2).delete() # filter 方法返回 QuerySet对象
        # 2. 清空表记录
        # ret = models.Book.objects.all().delete()
        # print(ret) # (18, {'root.Book': 18})

        """改 update"""
        # 1. QuerySet调用 update
        # ret = models.Book.objects.filter(id=21).update(**{'bname': '天才在左，疯子在右', 'publisher': '机械工业出版社'})
        # print(ret) # 1
        # 2. 错误示例： model对象调用
        # models.Book.objects.get(id=21).update(bname = '疯子') # AttributeError: 'Book' object has no attribute 'update'

        """查询"""
        # 1. all() 查询所有，返回值为 QuerySet集合
        # ret = models.Book.objects.all()
        # print(ret) # <QuerySet [<Book: 天才在左，疯子在右>, <Book: book2>, ...]>

        # 2.filter() 条件查询，返回值为 QuerySet集合，结果为空时返回空集合
        # ret = models.Book.objects.filter(price = 120.00)
        # print(ret) # <QuerySet [<Book: book20>, <Book: book21>]>
        # ret2 = models.Book.objects.filter(id=50)
        # print(ret2) # <QuerySet []>

        # 查询结果继续调用其他QuerySet方法
        # models.Book.objects.filter(id=21).update(price=110.00)
        # 多条件查询
        # ret = models.Book.objects.filter(**{'price': 110.00, 'publisher': '人民邮电出版社'})
        # print(ret) # <QuerySet [<Book: book10>]>

        # 3.get() 条件查询，返回值为 model对象，返回数据为多条时，抛异常
        # ret = models.Book.objects.get(id=21)
        # print(ret)
        # ret2 = models.Book.objects.get(publisher = '人民邮电出版社')
        # print(ret2) # get() returned more than one Book -- it returned 20!

        # 4. exclude(**kwargs) 排除符合条件的记录，支持 objects控制器和QuerySet 调用
        # ret = models.Book.objects.exclude(**{"publisher": '人民邮电出版社'})
        # print(ret) # <QuerySet [<Book: 天才在左，疯子在右>]>
        #
        # ret2 = models.Book.objects.filter(price=110.00).exclude(**{'publisher': '人民邮电出版社'})
        # print(ret2) # <QuerySet [<Book: 天才在左，疯子在右>]>

        # 5. order_by(*filed) 排序，默认升序， 字段前加上减号 按倒叙排列
        # ret = models.Book.objects.filter(publisher = "人民邮电出版社").order_by('-price', 'id') # 按 price 降序， id 升序
        # print(ret)

        # 6. reverse() 翻转结果集顺序，例如排序之后 翻转顺序
        # ret = models.Book.objects.all().order_by('price').reverse()
        # print(ret)

        # 7. count() 查询QuerySet 方法返回的结果集中的数据数量
        # ret = models.Book.objects.filter(publisher__regex='^人民邮电出版社$').count()
        # print(ret) # 10

        # 8. first() 返回 QuerySet集合的第一条记录， 返回值是 model对象
        # ret = models.Book.objects.all().first()
        # print(ret) # book1

        # 9. last() 返回 QuerySet集合的最后条记录， 返回值是 model对象
        # ret = models.Book.objects.all().last()
        # print(ret) # book20

        # 10. exists() 返回值 True / False, QuerySet结果集为空时返回False， 否则返回True，可用来判断 查询结果是否为空
        # ret = models.Book.objects.filter(bname = 'book20').exists()
        # print(ret) # True

        # 11. values(*filed) 返回可迭代的字典列表，返回值类型为 ValueQuerySet类型，相当于 pymysql游标加上参数 pymysql.cursor.DictCursor
        # ret = models.Book.objects.all().values(*('bname', 'publishDate')).filter(id__lt=2)
        # print(ret) # <QuerySet [{'bname': 'book1', 'publishDate': datetime.date(2017, 1, 1)}]>

        # 12. values_list(*filed) 返回元组列表
        # ret = models.Book.objects.all().values_list(*('bname', 'publishDate')).filter(id__lte=2)
        # print(ret) # <QuerySet [('book1', datetime.date(2017, 1, 1)), ('book2', datetime.date(2017, 1, 2))]>

        # 13. distinct() 去重， 对于QuerySet结果进行去重
        # ret = models.Book.objects.values('publisher').distinct()
        # print(ret) # <QuerySet [{'publisher': '机械工业出版社'}, {'publisher': '人民邮电出版社'}]>


        """双下划线方法"""
        # ret = models.Book.objects.filter(bname__iendswith=5)
        # print(ret) # <QuerySet [<Book: book5>, <Book: book15>]>

        # ret = models.Book.objects.filter(bname__in=['book1', 'book2'])
        # print(ret) # <QuerySet [<Book: book1>, <Book: book2>]>

        # ret = models.Book.objects.filter(id__gte=19)
        # print(ret) # <QuerySet [<Book: book19>, <Book: book20>]>

        # ret = models.Book.objects.filter(id__range=[1, 2])
        # print(ret) # <QuerySet [<Book: book1>, <Book: book2>]>

        # ret = models.Book.objects.filter(bname__contains='5')
        # print(ret) # <QuerySet [<Book: book5>, <Book: book15>]>

        # ret = models.Book.objects.filter(bname__startswith='book2')
        # print(ret) # <QuerySet [<Book: book2>, <Book: book20>]>

        # ret = models.Book.objects.filter(publishDate__year=2017, publishDate__month=1, publishDate__day__lte=5)
        # print(ret) # <QuerySet [<Book: book1>, <Book: book2>, <Book: book3>, <Book: book4>, <Book: book5>]>


        return render(request, 'login.html')

    def post(self, request):

        login_user = request.POST.get('username')
        login_pwd = request.POST.get('password')
        print(login_user, login_pwd)
        yn_exist = models.UserInfo.objects.filter(username=login_user).exists()
        if yn_exist:
            pwd = models.UserInfo.objects.filter(username=login_user).values('password')[0]['password']
            print(pwd)
            if login_pwd == pwd:
                all_books = models.Book.objects.all().values('bname', 'price', 'publishDate', 'publisher')
                print(all_books)
                return render(request, 'home.html', {'all_books': all_books})
            else:
                return HttpResponse('用户名或密码错误!')

        else:
            return HttpResponse('用户名或密码错误!')