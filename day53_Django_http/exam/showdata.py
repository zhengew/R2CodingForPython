# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: showdata.py
# @datatime: 2023/6/25 21:03

import pymysql

def showdata():
    conn = pymysql.connect(
        user= 'root',  # The first four arguments is based on DB-API 2.0 recommendation.
        password="123456",
        host= '172.16.238.5',
        database= 'day53',
        port= 3306,
        charset="utf8",
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from userinfo where id = %s"

    cursor.execute(sql, (1,))
    data = cursor.fetchone()
    print(data)
    cursor.close()
    conn.close()
    return data


if __name__ == '__main__':
    showdata()