from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.urls import reverse # 反向解析url
from root import models
# Create your views here.
import logging
logging.basicConfig(level=logging.DEBUG)

class RootApp(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super(RootApp, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return render(request, 'login.html')

        elif request.path == '/addBook/':
            all_publishs = self.query_all_publishs()
            all_authors = self.query_all_authors()
            return render(request, 'add_book.html', {'all_publishs': all_publishs, 'all_authors': all_authors})

        elif request.path == '/queryBook/':
            all_books = self.query_all_books()
            return render(request, 'home.html', {'all_books': all_books})

        elif request.path.startswith('/delBook/'):
            book_id = kwargs['book_id']
            root_book_authors_id = [id['authors__id'] for id in models.Book.objects.filter(id=book_id).values('authors__id')]
            # 删除中间表和书籍表
            models.Book.objects.get(id=book_id).authors.remove(*root_book_authors_id)
            models.Book.objects.filter(id=book_id).delete()
            # 重定向
            return redirect(reverse('queryBook'))

        elif request.path.startswith('/editBook/'):
            id = kwargs['book_id']
            book_obj = models.Book.objects.get(id=id)
            title = book_obj.title
            price = book_obj.price
            publishDate = book_obj.publishDate
            publishID = book_obj.publishs.id
            authorID = [book['id'] for book in book_obj.authors.values('id')]
            all_publishs = models.Publish.objects.all()
            all_authors = models.Author.objects.all()

            return render(request, 'edit_book.html', {'id': id, 'title': title, 'price': price,
                                                      'publishDate': publishDate, 'publishID': publishID,
                                                      'authorID': authorID, 'all_publishs': all_publishs,
                                                      'all_authors': all_authors})

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

        elif request.path.startswith('/editBook/'):
            id = kwargs['book_id']
            title = request.POST.get('bookName')
            price = request.POST.get('bookPrice')
            publishDate = request.POST.get('bookPublishDate')
            publishID = request.POST.get('selectBookPublisher')[0]
            author = request.POST.getlist('selectBookAuthor')
            # 修改书籍信息
            models.Book.objects.filter(id=id).update(
                title=title,
                price=price,
                publishDate=publishDate,
                publishs_id=publishID,
            )
            # 中间表 先删除再添加
            book_obj = models.Book.objects.get(id=id)
            book_obj.authors.clear()
            book_obj.authors.add(*author)

            # 重定向到查询页面
            return redirect(reverse('queryBook'))

    # 查询所有书籍信息
    def query_all_books(self):
        all_books = models.Book.objects.all().values('id', 'title', 'price', 'publishDate', 'publishs__name', 'authors__name').order_by('id') # TODO: 联名作者需要处理下，作者名,分隔
        booksID = set()
        ret = {}
        for book in all_books:
            id = book['id']
            if id not in booksID:
                ret[id] = book
                booksID.add(id)
            elif id in booksID:
                ret[id]['authors__name'] = ', '.join([ret[id]['authors__name'], book['authors__name']])
        all_books = [book for book in ret.values()]
        return all_books

    # 查询所有出版社
    def query_all_publishs(self):
        ret = models.Publish.objects.all().values('id', 'name')
        return ret

    # 查询所有作者
    def query_all_authors(self):
        ret = models.Author.objects.all().values('id', 'name')
        return ret