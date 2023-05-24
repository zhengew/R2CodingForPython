# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 演示pymysql模块.py
# @datatime: 2023/5/24 12:37

'''
演示pymysql模块
'''

import pymysql
from warnings import filterwarnings
import logging

# 设置日志级别
logging.basicConfig(level=logging.DEBUG)
# 忽略mysql告警信息
filterwarnings('ignore', category=pymysql.Warning)

class MysqlDB(object):

    def __init__(self):
        try:
            self.conn = pymysql.connect(  # 建立连接
                user='root',
                password='123456',
                host='172.16.238.5',
                database='homework',
            )
            # 使用cursor方法操作游标，得到一个可执行的sql语句,并且操作结果以字典列表返回的游标
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 获取游标
        except Exception as e:
            logging.debug('数据库连接失败，失败原因:%s' %e)
    def __del__(self):
        """回收对象"""
        try:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()
        except Exception as e:
            logging.debug('数据库连接失败,失败原因:%s' %e)

    def query(self, sql: str, *args, state='all'):
        """
        查询
        :param sql:
        :param args: sql语句%s替换的内容，execute接收的实参
        :param state: all 默认查询全部
        :return:
        """
        try:
            self.cur.execute(sql, args)

            if state == 'all':
                # 查询全部
                data = self.cur.fetchall()
            else:
                # 查询单条
                data = self.cur.fetchone()
            return data

        except Exception as e:
            logging.debug('数据库连接失败,失败原因:%s' %e)


    def execute(self, sql: str, *args):
        """
        更新 删除 修改
        :param sql:
        :param args: sql语句%s替换的内容，execute接收的实参
        :return:
        """
        try:
            # 使用execute执行sql
            rows = self.cur.execute(sql, args)
            # 提交事物
            self.conn.commit()
            return rows # 执行sql影响的行
        except Exception as e:
            logging.debug('数据库连接失败，失败原因:%s' %e)
            # 如果事物异常，则回滚事物
            self.conn.rollback()

if __name__ == '__main__':
    sql = 'select * from teacher where tid in( %s, %s, %s)'
    db = MysqlDB()
    data = db.query(sql, 1, 2, 3)
    print(data)

    # sql2 = 'insert into teacher (tname) values(%s)'
    # rows = db.execute(sql2, 'taibai')
    # print(rows)