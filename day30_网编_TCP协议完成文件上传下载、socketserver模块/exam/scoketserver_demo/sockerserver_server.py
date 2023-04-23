# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: sockerserver_server.py
# @datatime: 2023/4/23 07:54

"""
目标: 掌握 socketserver模块的server端代码结构
"""
import socketserver
import time

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        # handle方法内执行与客户端交互的逻辑
        conn = self.request # 服务端的三次握手
        while True:
            # 每个线程服务与客户端交互
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(0.5)
            except ConnectionResetError:
                break

server = socketserver.ThreadingTCPServer(('127.0.0.1', 8081), Myserver) # 实例化服务
server.serve_forever() # 启动服务