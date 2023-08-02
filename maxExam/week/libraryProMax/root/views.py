from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.urls import reverse # 反向解析url
from root import models
# Create your views here.

class RootApp(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super(RootApp, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return render(request, 'login.html')

    def post(self, request, *args, **kwargs):

        if request.path == '/':
            loginName = request.POST.get('username')
            loginPwd = request.POST.get('password')
            if models.UserInfo.objects.filter(username=loginName).exists():
                pwd = models.UserInfo.objects.filter(username=loginName).values('password')[0]['password']
                if loginPwd == pwd:
                    all_books = self.query_all_books()
                    return render(request, 'home.html', {'all_books': all_books})
                else:
                    return redirect('login')
            else:
                return redirect(reverse('login'))



    def query_all_books(self):
        '''
        select
	        rb.title, rb.price, rb.publishDate, rp.name as publishName, ra.name as authorName
         from root_book rb
         inner join root_publish rp on rb.publishs_id = rp.id
         inner join root_book_authors rba  on rb.id = rba.book_id
         inner join root_author ra on rba.author_id = ra.id
         order by rb.id asc
        '''

        ret = models.Book.objects.all().values('title', 'price', 'publishDate', 'publishs__name', 'authors__name')
        print(ret)
        return ret
