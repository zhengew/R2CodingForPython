# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 08_wsgiref升级版web框架.py
# @datatime: 2023/6/25 21:21

import socket
from threading import Thread
import time
from wsgiref.simple_server import make_server
from jinja2 import Template
from showdata import showdata


server = socket.socket()
ip_port = ('127.0.0.1', 8081)
server.bind(ip_port)
server.listen()

def html():
    userinfo_data = showdata()
    print(userinfo_data)
    with open('08_jinja2动态页面web框架.html', 'r') as f:
        data = f.read()
    tem = Template(data)
    data = tem.render({'userinfo':userinfo_data})
    # data = data.replace('$tag$', time.strftime('%Y-%m-%d %H:%M:%S')).encode('utf-8')
    data = data.encode('utf-8')
    return data

def css():
    with open('day53.css', 'rb') as f:
        data = f.read()
    return data
def js():
    with open('day53.js', 'rb') as f:
        data = f.read()
    return data
def icon():
    with open('myicon.ico', 'rb') as f:
        data = f.read()
    return data
def img():
    with open('background-img.png', 'rb') as f:
        data = f.read()
    return data

url_patters = [
    ('/', html),
    ('/day53.css', css),
    ('/day53.js', js),
    ('/background-img.png', img),
    ('/myicon.ico', icon),
]


def application(environ, start_reponse):
    start_reponse('200 SUCCESS', [('username', 'zew'), ('password', '123')])
    path = environ['PATH_INFO']

    for i in url_patters:
        if i[0] == path:
            ret = i[1]()
            break
    else:
        ret = b'404 not fond'
    return [ret]

httpd = make_server('127.0.0.1', 8080, application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()


