# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 线程池案例.py
# @datatime: 2023/5/1 17:24

from concurrent.futures import ThreadPoolExecutor
import requests
import os

def get_page(url):    # 访问网页,获取网页源代码   线程池中的线程来操作
    print('<进程%s> get %s' %(os.getpid(),url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url':url,'text':respone.text}

def parse_page(res):   # 获取到字典结果之后,计算网页源码的长度,把https://www.baidu.com : 1929749729写到文件里   线程任务执行完毕之后绑定回调函数
    res=res.result()
    print('<进程%s> parse %s' %(os.getpid(),res['url']))
    parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
    with open('db.txt','a') as f:
        f.write(parse_res)

if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    # 线程池
    tp = ThreadPoolExecutor(5)
    for url in urls:
        ret = tp.submit(get_page, url)      # 循环url列表,拿到future对象
        ret.add_done_callback(parse_page)   # future对象绑定回掉函数 pase_page