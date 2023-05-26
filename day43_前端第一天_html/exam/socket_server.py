# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: socket_server.py
# @datatime: 2023/5/26 下午12:10
import os.path
import socketserver
import logging

logging.basicConfig(level=logging.DEBUG)

class MyServer(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        conn = self.request
        logging.info('当前链接客户端:%s' %conn)
        try:
            path = os.path.join(os.path.dirname(__file__), 'html_exam', 'form表单.html')
            data = self.read_html(path)
            req_client = conn.recv(1024).decode('utf-8')
            print(req_client)
            conn.send(data)

        except ConnectionResetError as e:
            logging.debug(e)

    def read_html(self, path):
        """
        读取html
        :param path:
        :return:
        """
        with open(path, mode='rb') as f:
            data = f.read()
        print(data)
        return data

def run():
    server = socketserver.ThreadingTCPServer(('172.17.0.1', 8083), MyServer)
    server.serve_forever()

if __name__ == '__main__':
    run()