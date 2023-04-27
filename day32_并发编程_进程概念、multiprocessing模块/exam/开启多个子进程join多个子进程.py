# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 开启多个子进程join多个子进程.py
# @datatime: 2023/4/27 下午4:33
"""
目标:阻塞子进程 join方法
同步阻塞
"""
from multiprocessing import Process
def send_email(num):
    print(f"开始发送第{num}封邮件~")
if __name__ == '__main__':
    p_lst = []
    for i in range(1, 5):
        p = Process(target=send_email, args=(i,))
        p.start() # 异步非阻塞，不需要等待子进程结束就可以继续开启其他子进程
        p_lst.append(p)

    for p in p_lst:
        p.join()  # 阻塞子进程方法，同步阻塞，必须等待全部子进程执行完毕，才会打印 全部邮件发送完毕～
    print('全部邮件发送完毕～')