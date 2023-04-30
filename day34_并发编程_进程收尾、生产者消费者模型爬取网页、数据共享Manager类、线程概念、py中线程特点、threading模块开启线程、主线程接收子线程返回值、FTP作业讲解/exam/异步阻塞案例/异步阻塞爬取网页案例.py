# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 异步阻塞爬取网页案例.py
# @datatime: 2023/4/30 10:03

"""
目标:通过生产者消费者模型演示异步阻塞
"""
from multiprocessing import Process, Queue, set_start_method
import requests

url_dict = {
    'hao123': 'https://www.hao123.com/?src=from_pc_logon',
    'sina': 'https://news.sina.com.cn/',
    'anjuke':'https://beijing.anjuke.com/?pi=navi-hao123-mz'

}
def consumer(q): # 消费者
    while True:
        ret = q.get()
        if ret:
            with open('%s.html'%ret[0], mode='wt', encoding='utf-8') as f:
                f.write(ret[1])
        else:
            break
def procucter(name, url, q): # 生产者
    ret = requests.get(url, )
    q.put((name, ret.text))

if __name__ == '__main__': # 主进程
    p_lst = []
    q = Queue()
    for key in url_dict:
        p = Process(target=procucter, args=(key, url_dict[key], q))
        p.start() # 异步非阻塞 启动 生产者
        p_lst.append(p)
    Process(target=consumer, args=(q,)).start() # 异步非阻塞
    for p in p_lst: p.join() # 异步阻塞， 消费者异步消费，每消费完一次进入阻塞状态，直到全部消费完毕，接收None在终止消费进程
    q.put(None) # 结束消费者进程阻塞状态

