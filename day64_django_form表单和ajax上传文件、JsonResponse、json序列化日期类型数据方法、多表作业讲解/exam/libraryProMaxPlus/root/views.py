from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse # url 方向解析
from django.http import JsonResponse # json响应
from django.utils.decorators import method_decorator # 装饰器
from django.db import transaction
from django.views import View
from root import models

# Create your views here.

class RootView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return render(request, 'login.html')
        elif request.path == '/showBooks/':
            all_books = models.Book.objects.all()
            return render(request, 'showBooks.html',{'all_books':all_books})
        elif request.path == '/addBook/':
            all_publishs = models.Publish.objects.all()
            all_authors = models.Author.objects.all()
            return render(request, 'addBook.html', {"all_publishs": all_publishs, "all_authors": all_authors})
        elif request.path.startswith('/editBook/'):
            book_id = kwargs['id']
            book = models.Book.objects.get(id=book_id)
            all_publishs = models.Publish.objects.all()
            all_authors = models.Author.objects.all()
            return render(request, 'editBook.html', {'book': book, 'all_publishs': all_publishs, 'all_authors': all_authors})

        elif request.path.startswith('/delBook/'):
            book_id = kwargs['id']
            with transaction.atomic():
                book_obj = models.Book.objects.get(id=book_id)
                book_obj.delete()
            return redirect('showBooks')


    def post(self, request, *args, **kwargs):

        if request.path == '/':
            data = request.POST.dict()
            loginName = data['username']
            loginPwd = data['password']
            yn_exist = models.UserInfo.objects.filter(username=loginName).exists()
            if yn_exist:
                password = models.UserInfo.objects.get(username=loginName).password
                if password == loginPwd:
                    res = {'RETCODE': '200', 'DATA': '/showBooks/', 'RETMSG': 'SUCCESS'}
                elif loginPwd.strip() == '':
                    res = {'RETCODE': 'PASSWORD_IS_NULL_ERROR', 'DATA': '', 'RETMSG': '请输入密码'}
                else:
                    res = {'RETCODE': 'USERNAME_OR_PASSWORD_ERROR', 'DATA': '', 'RETMSG': '用户名或密码错误'}
            elif loginName.strip() == '':
                res = {'RETCODE': 'USERNAME_IS_NULL_ERROR', 'DATA': '', 'RETMSG': '请输入用户名'}
            else:
                res = {'RETCODE': 'USERNAME_OR_PASSWORD_ERROR', 'DATA': '', 'RETMSG': '用户名或密码错误'}

            return JsonResponse(res)

        elif request.path == '/addBook/':
            authors_name = request.POST.getlist('authors')
            data = request.POST.dict()
            del data['csrfmiddlewaretoken']
            del data['authors']
            yn_book_exist = models.Book.objects.filter(bname=data['bname']).exists()
            if not yn_book_exist:
                if data['price'].strip() == '':
                    res = {'RETCODE': 'BOOK_PRICE_IS_NULL_ERROR', 'RETMSG': '价格不能为空'}
                elif float(data['price']) <= 0:
                    res = {'RETCODE': 'BOOK_PRICE_LESS_THAN_ZERO_ERROR', 'RETMSG': '价格不能为0或负数'}
                elif len(authors_name) == 0:
                    res = {'RETCODE': 'BOOK_AUTHOR_IS_NULL_ERROR', 'RETMSG': '作者不能为空'}
                elif data['publishDate'] == '':
                    res = {'RETCODE': 'BOOK_PUBLISHDATE_IS_NULL_ERROR', 'RETMSG': '出版日期不能为空'}
                else:
                    res = {'RETCODE': '200', 'DATA': '/showBooks/', 'RETMSG': 'SUCCESS'}
            elif data['bname'].strip() == '':
                res = {'RETCODE': 'BOOK_NAME_IS_NULL_ERROR', 'RETMSG': '书籍名称不能为空'}
            else:
                res = {'RETCODE': 'BOOK_IS_EXISTS_ERROR', 'DATA': '', 'RETMSG': '系统中已存在同名书籍'}

            # 插入数据
            if res['RETCODE'] == '200':
                with transaction.atomic():  # 开启事物
                    book_Obj = models.Book.objects.create(**data)
                    book_Obj.authors.add(*authors_name)

            return JsonResponse(res)

        elif request.path.startswith('/editBook/'):
            book_id = kwargs['id']
            authors_name = request.POST.getlist('authors')[0].replace("'", "").split(',')
            print(authors_name)
            data = request.POST.dict()
            del data['csrfmiddlewaretoken']
            del data['authors']
            print(data)
            book_Obj = models.Book.objects.filter(id=book_id)

            book_exist_gt_2 = True if models.Book.objects.filter(bname=data['bname']).count() >= 2 else False
            if not book_exist_gt_2:
                if data['price'].strip() == '':
                    res = {'RETCODE': 'BOOK_PRICE_IS_NULL_ERROR', 'RETMSG': '价格不能为空'}
                elif float(data['price']) <= 0:
                    res = {'RETCODE': 'BOOK_PRICE_LESS_THAN_ZERO_ERROR', 'RETMSG': '价格不能为0或负数'}
                elif len(authors_name) == 0:
                    res = {'RETCODE': 'BOOK_AUTHOR_IS_NULL_ERROR', 'RETMSG': '作者不能为空'}
                elif data['publishDate'] == '':
                    res = {'RETCODE': 'BOOK_PUBLISHDATE_IS_NULL_ERROR', 'RETMSG': '出版日期不能为空'}
                else:
                    res = {'RETCODE': '200', 'DATA': '/showBooks/', 'RETMSG': 'SUCCESS'}
            elif data['bname'].strip() == '':
                res = {'RETCODE': 'BOOK_NAME_IS_NULL_ERROR', 'RETMSG': '书籍名称不能为空'}
            else:
                res = {'RETCODE': 'BOOK_IS_EXISTS_ERROR', 'DATA': '', 'RETMSG': '系统中已存在同名书籍'}

            if res['RETCODE'] == '200':
                with transaction.atomic():  # 开启事物
                    book_Obj.update(**data)
                    book_Obj.first().authors.set(authors_name)

            return JsonResponse(res)