from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from root import models

class Library(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        if request.path == '/':
            return render(request, 'login.html')
        elif request.path == '/addBook/':
            return render(request, 'add_book.html')

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
                    all_books = models.Book.objects.all().values('bname', 'price', 'publishDate', 'publisher')
                    print(all_books)
                    return render(request, 'home.html', {'all_books': all_books})
                else:
                    return HttpResponse('用户名或密码错误!')

            else:
                return HttpResponse('用户名或密码错误!')
        elif request.path == '/addBook/':
            print(request.body)
            bname = request.POST.get('inputBookName')
            price = request.POST.get('inputBookPrice')
            publishDate = request.POST.get('inputBookPublishDate')
            publisher = request.POST.get('inputBookPublisher')
            print(bname, price, publishDate, publisher)
            return HttpResponse('/addBook/')
