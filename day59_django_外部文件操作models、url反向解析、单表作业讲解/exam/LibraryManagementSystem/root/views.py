from audioop import reverse

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from root import models

from django.urls import reverse # url别名反向解析


class Library(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        if request.path == '/':
            # 1 查询某某出版社出版过的价格大于200的书籍
            ret = models.Book.objects.filter(publisher='机械工业出版社', price__gt=200)
            print(ret)
            # 2 查询2017年8月出版的所有以py开头的书籍名称
            ret = models.Book.objects.filter(publishDate__year=2017, publishDate__month=8, bname__istartswith='py').values('bname')
            print(ret)
            # 3 查询价格为50,100或者150的所有书籍名称及其出版社名称
            ret = models.Book.objects.filter(price__in=[50, 100, 150]).values('bname', 'publisher')
            print(ret)
            # 4 查询价格在100到200之间的所有书籍名称及其价格
            ret = models.Book.objects.filter(price__range=[100, 200]).values('bname', 'price')
            print(ret)
            # 5 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
            ret = models.Book.objects.filter(publisher='人民出版社').values('price').distinct().order_by('-price')
            print(ret)
            return render(request, 'login.html')
        elif request.path == '/addBook/':
            return render(request, 'add_book.html')
        elif 'editBook' in request.path:
            book_id = int(request.GET.get('id'))
            print(book_id, type(book_id))
            book_info = models.Book.objects.filter(id=book_id).values('bname', 'price', 'publishDate', 'publisher').first()
            return render(request, 'edit_book.html', {'id': book_id, 'bname': book_info['bname'], 'price': book_info['price'], 'publishDate': book_info['publishDate'], 'publisher': book_info['publisher']})

        elif request.path == '/showBook/':
            all_books = self.query_all_books()
            return render(request, 'home.html', {'all_books': all_books})

        elif 'removeBook' in request.path:
            book_id = int(request.GET.get('id'))
            models.Book.objects.filter(id=book_id).delete()

            # all_books = self.query_all_books()
            # return render(request, 'home.html', {'all_books': all_books})
            # 重定向
            return redirect(reverse('showBooks'))  # url别名反向解析: reverse('别名')

    def post(self, request):
        if request.path == '/':
            login_user = request.POST.get('username')
            login_pwd = request.POST.get('password')
            print(login_user, login_pwd)
            yn_exist = models.UserInfo.objects.filter(username=login_user).exists()
            if yn_exist:
                pwd = models.UserInfo.objects.filter(username=login_user).values('password')[0]['password']
                print(pwd)
                if login_pwd == pwd:
                    all_books = self.query_all_books()
                    return render(request, 'home.html', {'all_books': all_books})
                else:
                    return HttpResponse('用户名或密码错误!')

            else:
                return HttpResponse('用户名或密码错误!')
        elif request.path == '/addBook/':
            bname = request.POST.get('inputBookName')
            price = request.POST.get('inputBookPrice')
            publishDate = request.POST.get('inputBookPublishDate')
            publisher = request.POST.get('inputBookPublisher')
            print(bname, price, publishDate, publisher)
            # 添加书籍
            models.Book.objects.create(**{'bname': bname, 'price': price, 'publishDate': publishDate, 'publisher': publisher})
            # all_books = self.query_all_books()
            # return render(request, 'home.html', {'all_books': all_books})
            # 重定向
            return redirect(reverse('showBooks')) # url别名反向解析: reverse('别名')

        elif 'editBook' in request.path:
            id = request.POST.get('inputBookID')
            models.Book.objects.filter(id=id).update(**{
                'bname': request.POST.get('inputBookName'),
                'price': request.POST.get('inputBookPrice'),
                'publishDate': request.POST.get('inputBookPublishDate'),
                'publisher': request.POST.get('inputBookPublisher'),
            })
            # all_books = self.query_all_books()
            # return render(request, 'home.html', {'all_books': all_books})
            # 重定向
            return redirect(reverse('showBooks'))  # url别名反向解析: reverse('别名')

    def query_all_books(self):
        """
        查询所有书籍
        :return:
        """
        all_books = models.Book.objects.all().values('id', 'bname', 'price', 'publishDate', 'publisher')
        return all_books