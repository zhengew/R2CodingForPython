# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: pymysql_exam.py
# @datatime: 2023/5/22 22:11

import pymysql

# 建立连接
conn = pymysql.connect( user='root',
                        password='123456',
                        host='172.16.238.5',
                        database='homework',)

# 创建游标
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor) # 查询返回字典，表字段名作为key
cur = conn.cursor()


# 异常处理
try:
    cur.execute('select * from student')
    ret = cur.fetchone() # 获取一条结果
    print(ret)

    ret2 = cur.fetchmany(3) # 获取多条结果，需指定size
    print(ret2)
    ret3 = cur.fetchall() # 获取全部结果
    print(ret3)
except pymysql.err.ProgrammingError as e:
    print(e) # (1146, "Table 'homework.students' doesn't exist")

