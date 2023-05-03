# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 回掉函数例子.py
# @datatime: 2023/5/3 14:34

"""
目标:掌握回掉函数用户
1.多线程异步非阻塞获取网页源代码
2.异步阻塞解析网页内容并存储到文件中
"""
from concurrent.futures import ThreadPoolExecutor
import requests
from threading import current_thread
def get_page(url):
    print('<线程%s> get %s' %(current_thread().ident, url))
    response = requests.get(url)
    if response.status_code == 200:
        return {'url': url, 'text': response.text}
def parse_url(res): # 异步阻塞 执行回掉函数
    ret = res.result()
    print('<线程%s> parse %s' %(current_thread().ident, ret['url']))
    parse_res='url:<%s> size:[%s]\n' %(ret['url'],len(ret['text']))
    with open('parse_url.txt', mode='at', encoding='utf-8') as f:
        f.write(parse_res)

if __name__ == '__main__':
    url_lst=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    tp = ThreadPoolExecutor(4) # 线程池
    for url in url_lst: # 异步非阻塞
        res = tp.submit(get_page, url)
        res.add_done_callback(parse_url) # 绑定回掉函数










