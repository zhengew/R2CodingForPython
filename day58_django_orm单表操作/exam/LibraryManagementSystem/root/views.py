from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from root import models

class Library(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):

        # 新增
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