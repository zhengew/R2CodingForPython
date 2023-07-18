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
            return render(request, 'login.html')

        elif request.path == '/showBooks/':
            allBooks = models.Book.objects.all()
            return render(request, 'showBooks.html', {'allBooks': allBooks})

        elif request.path == '/addBook/':
            return render(request, 'addBooks.html')

        elif '/editBook/' in request.path:

            book_id = kwargs['id']
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


