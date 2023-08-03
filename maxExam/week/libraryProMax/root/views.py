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

        elif request.path == '/addBook/':
            all_publishs = self.query_all_publishs()
            print(all_publishs)
            all_authors = self.query_all_authors()
            return render(request, 'add_book.html', {'all_publishs': all_publishs, 'all_authors': all_authors})

        elif request.path == '/queryBook/':
            all_books = self.query_all_books()
            return render(request, 'home.html', {'all_books': all_books})

        elif request.path.startswith('/delBook/'):
            book_id = kwargs['book_id']
            root_book_authors_id = [id['authors__id'] for id in models.Book.objects.filter(id=book_id).values('authors__id')]
            print(root_book_authors_id)
            # 删除中间表和书籍表
            models.Book.objects.get(id=book_id).authors.remove(*root_book_authors_id)
            models.Book.objects.filter(id=book_id).delete()
            # 重定向
            return redirect(reverse('queryBook'))


    def post(self, request, *args, **kwargs):

        if request.path == '/':
            loginName = request.POST.get('username')
            loginPwd = request.POST.get('password')
            if models.UserInfo.objects.filter(username=loginName).exists():
                pwd = models.UserInfo.objects.filter(username=loginName).values('password')[0]['password']
                if loginPwd == pwd:
                    return redirect(reverse('queryBook'))
                else:
                    return redirect(reverse('login'))
            else:
                return redirect(reverse('login'))

        elif request.path == '/addBook/': # TODO: 添加书籍 作者有多个的时候需要拼接作者姓名，现在是重复添加了多条数据，明天改
            bookName = request.POST.get('inputBookName')
            if not models.Book.objects.filter(title=bookName).exists():
                bookPrice = request.POST.get('inputBookPrice')
                bookPublishDate = request.POST.get('inputBookPublishDate')
                bookPublish = request.POST.get('selectBookPublisher')
                bookAuthors = request.POST.getlist('selectBookAuthor')
                # 书籍
                models.Book.objects.create(**{'title': bookName, 'price': bookPrice, 'publishDate': bookPublishDate,
                                              'publishs_id': bookPublish})
                # 作者
                models.Book.objects.get(title=bookName).authors.add(*bookAuthors)
                # 重定向
                return redirect(reverse('queryBook'))
            else:
                return redirect(reverse('queryBook'))




    # 查询所有书籍信息
    def query_all_books(self):
        '''
        select
	        rb.title, rb.price, rb.publishDate, rp.name as publishName, ra.name as authorName
         from root_book rb
         inner join root_publish rp on rb.publishs_id = rp.id
         inner join root_book_authors rba  on rb.id = rba.book_id
         inner join root_author ra on rba.author_id = ra.id
         order by rb.id
        '''

        ret = models.Book.objects.all().values('id', 'title', 'price', 'publishDate', 'publishs__name', 'authors__name')
        return ret

    # 查询所有出版社
    def query_all_publishs(self):
        ret = models.Publish.objects.all().values('id', 'name')
        return ret

    # 查询所有作者
    def query_all_authors(self):
        ret = models.Author.objects.all().values('id', 'name')
        return ret