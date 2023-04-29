# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 进程之间数据安全问题例子.py
# @datatime: 2023/4/29 11:39

"""
目标: 理解为什么进程之间存在数据安全问题，以及通过枷锁解决进程之间数据安全问题
# mac系统需要手动设置py进程启动方式为 fork
# 抢票例子
"""
import time
from multiprocessing import Process, Lock, set_start_method
import json
def search_ticket(i):
    with open('ticket', mode='rt', encoding='utf-8') as f:
        tickets = json.load(f)
    print('%s:当前余票是%s张' %(i, tickets['count']))
def buy_ticket(i):
    with open('ticket', mode='rt', encoding='utf-8') as f:
        tickets = json.load(f)
    if tickets['count'] > 0:
        tickets['count'] -= 1
        print('%s买到票了' % i)
    time.sleep(0.2)
    with open('ticket', mode='wt',encoding='utf-8') as f:
        json.dump(tickets, f)

def get_ticket(i, lock):
    search_ticket(i) # 查询余票不需要加锁
    with lock: # 买票需要加锁保证数据安全，避免票据超发，出现多个人买一张票的情况
        buy_ticket(i)

if __name__ == '__main__':
    set_start_method('fork') # 设置进程启动方式为 fork
    lock = Lock()
    for i in range(3):
        Process(target=get_ticket, args=(i,lock)).start()





























