from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.urls import reverse # url别名反向解析

from root import models

# Create your views here.
class RootView(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        if request.path == '/':
            # new_author_detail = models.AuthorDetail.objects.create(
            #     birthday='1990-01-01',
            #     mobile='18712341234',
            #     address='北京市海淀区软件园二期东区17号楼'
            # )
            # author_detail_obj = models.AuthorDetail.objects.filter(mobile='18712341234').first()

            # 1.增
            # 1.1 一对一关系
            # 方式一 model对象

            # models.Author.objects.create(
            #     name='唐家三少',
            #     sex='1',
            #     authorDetail=author_detail_obj # 赋值为 model对象
            # )
            #
            # # 方式二 表中的外键字段=model对象.id
            # models.Author.objects.create(
            #     name='唐家三少',
            #     sex='1',
            #     authorDetail_id=author_detail_obj.id, # 表中的外键id 直接赋值 外键表的主键
            # )
            #

            # 1.2 一对多关系
            # publish_obj = models.Publish.objects.get(id=1)
            # author_detail_obj = models.AuthorDetail.objects.filter(mobile='18712341234').first()
            #
            # # 方式一 model对象
            # models.Book.objects.create(
            #     bname='完美世界',
            #     publishDate='2019-01-01',
            #     price=100.50,
            #     publish=publish_obj,
            # )
            #
            # # 方式二 model对象.id
            # models.Book.objects.create(
            #     bname='完美世界',
            #     publishDate='2019-01-01',
            #     price=100.50,
            #     publish_id=publish_obj.id,
            # )

            # 1.3 多对多关系
            # book_obj = models.Book.objects.get(bname='完美世界')
            # # 方式一 model对象.属性名.add(*[外键id, ...])
            # book_obj.author.add(*[3, 1])
            #
            # # 方式二 add方法中传 model对象
            # author1 = models.Author.objects.get(id=3)
            # author2 = models.Author.objects.get(id=1)
            #
            # book_obj.author.add(*[author1, author2])

            # 2.删除
            # 2.1 一对一、一对多同 单表删除, 一对一和一对多都是先删除外键所在的表，在删除本表
            # 一对一
            # models.AuthorDetail.objects.get(id=3).delete()
            # models.Author.objects.filter(name='唐家三少').delete()

            # 一对多
            # models.Publish.objects.get(id=1).delete()
            # models.Book.objects.get(id=3).delete()

            ##  多对多删除
            # 数据准备
            # book_obj = models.Book.objects.get(id=5)
            # author_obj = models.AuthorDetail.objects.create(
            #     birthday='1991-01-01',
            #     mobile='18712311231',
            #     address='河北省保定市',
            # )
            #
            # models.Author.objects.create(
            #     name='我吃西红柿',
            #     sex='1',
            #     authorDetail_id=author_obj.id
            # )
            # models.Book.objects.get(bname='完美世界').author.add(*[6, 7])

            book_obj = models.Book.objects.get(id=5)
            # remove
            # book_obj.author.remove(7)
            # book_obj.author.remove(*[6, 7])

            # clear 清空
            # book_obj.author.clear()

            # set 先清空中间表再插入数据
            # book_obj.author.set('6')
            # book_obj.author.set([6, ])

            # 3. 更新
            # 一对一更新
            # models.Author.objects.filter(id=6).update(
            #     name='辰东',
            #     sex = '1',
            #     authorDetail_id = 7,
            # )

            # 一对多更新
            # models.Book.objects.filter(pk=5).update(
            #     publish_id = 3,
            # )

            # 更新外键所在表的数据时，若没有做级联更新，会报错，这种可以用原生sql处理
            # 1451, 'Cannot delete or update a parent row: a foreign key constraint fails (`libraryms`.`root_book`, CONSTRAINT `root_book_publish_id_666b9e6e_fk_root_publish_id` FOREIGN KEY (`publish_id`) REFERENCES `root_publish` (`id`))')
            models.Publish.objects.filter(pk=3).update(
                id=1,
            )


            return render(request, 'login.html')

        elif request.path == '/showBooks/':
            allBooks = models.Book.objects.all()
            return render(request, 'showBooks.html', {'allBooks': allBooks})

        elif request.path == '/addBook/':
            return render(request, 'addBooks.html')

        elif '/editBook/' in request.path:

            book_id = kwargs['id'] # url中的参数由 **kwargs接收
            print(book_id)
            book_obj = models.Book.objects.get(id=book_id)
            return render(request, 'editBook.html', {'book': book_obj})

    def post(self, request, *args, **kwargs):
        if request.path == '/':
            loginName = request.POST.get('loginName')
            loginPassword = request.POST.get('loginPassword')
            yn_exists = models.UserInfo.objects.filter(username=loginName).exists()
            print(loginName, loginPassword, yn_exists)
            if yn_exists:
                pwd = models.UserInfo.objects.get(username=loginName).password
                if loginPassword == pwd:
                    return redirect(reverse('showBooks')) # 重定向到 showBooks页面
                else:
                    return redirect(reverse('login'))  # 重定向到 登录页
            else:
                return redirect(reverse('login')) # 重定向到 登录页
        elif request.path == '/addBook/':

            print(request.path)
            print(request.body)

            return HttpResponse('200 ok')


