from django.shortcuts import render, HttpResponse

from app01 import models
# Create your views here.

def query(request):
    # 多表 增删改查
    # 1. 增
    # 1.1 一对一增加

    # new_author_detail = models.AuthorDetail.objects.create(
    #     birthday='2010-01-01',
    #     telephone='18711113333',
    #     addr='北京市丰台区丰台科技园',
    # )

    # obj = models.AuthorDetail.objects.filter(addr='北京市海淀区肖家河西区').first()
    # print(obj)
    # # 方式一
    # models.Author.objects.create(
    #     name='苏轼',
    #     age='40',
    #     authorDetail=new_author_detail,
    # )

    # 方式二 常用
    # models.Author.objects.create(
    #     name='李白',
    #     age='44',
    #     authorDetail_id=obj.id, # mysql中的字段名=查询出来的queryset集合中的id
    # )

    # 一对多关系
    # 方式一
    obj = models.Publish.objects.get(id=1)

    # models.Book.objects.create(
    #     title='计算机组成原理',
    #     publishDate='2019-01-01',
    #     price=101.50,
    #     # publishs=models.Publish.objects.get(id=1),
    #     publishs=obj,
    # )
    #
    # 方式二 常用
    # models.Book.objects.create(
    #     title='django基础',
    #     publishDate='2019-01-01',
    #     price=101.50,
    #     # publishs=models.Publish.objects.get(id=1),
    #     publishs_id=obj.id,
    # )

    # 多对多关系
    # 方式一 常用
    # book_obj = models.Book.objects.get(nid=1)
    # book_obj.authors.add(
    #     *[1, 2] # 打散 author表id
    # )
    #
    # # 方式二
    # author1 = models.Author.objects.get(id=1)
    # author2 = models.Author.objects.get(id=2)
    #
    # book_obj = models.Book.objects.get(nid=5)
    # book_obj.authors.add(*[author1, author2])


    # 2. 删除
    # 一对一（外键+唯一）: 表一外键关联到表2 ，表一删除不影响表2，表2删除会影响表1
    # models.AuthorDetail.objects.filter(id=2).delete()
    # models.Author.objects.filter(id=3).delete()

    # 一对多（外键）
    # models.Book.objects.filter(nid=1).delete()
    # models.Publish.objects.filter(id=2).delete()

    # 多对多删除
    # 方式一
    # book_obj = models.Book.objects.get(nid=5)
    # book_obj.authors.remove(*[1, 5]) # 打散删除  参数对应的 外键id

    # 方式二
    # book_obj.authors.clear()

    # 方式三 先清空、再添加
    # book_obj.authors.set('1')
    # book_obj.authors.set(['5', '7']) # 清空+添加多个记录，不需要打散


    # 3.更新
    # 一对一更新
    # models.Author.objects.filter(id='5').update(
    #     name='崔雪飞',
    #     age=16,
    #     # authorDetail=models.AuthorDetail.objects.get(id=4),
    #     authorDetail_id=8,
    # )

    # 一对多
    # models.Book.objects.filter(pk=3).update(
    #     title='降龙十八掌第三式亢龙有悔',
    #     # publishs=models.Publish.objects.get(id=2),
    #     publishs_id=1,
    # )

    # 级联更新
    # models.Publish.objects.filter(pk=2).update(
    #     id=1, # django orm 没有级联更新, 需要在mysql中单独设置级联更新
    # )


    return HttpResponse('200 ok')