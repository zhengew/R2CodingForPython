import pymysql
import django
import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryProMaxPlus.settings')
    django.setup()

    from root import models

    book_obj = models.Book.objects.get(bname='天龙八部')

    ret = ','.join([author.name for author in book_obj.authors.all()])
    print(ret)