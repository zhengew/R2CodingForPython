# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: online_chat_server.py
# @datatime: 2023/4/18 20:11

"""
目标: 基于UDP协议实现多人聊天，要求切换IP后依然可以识别到用户(不依赖ip和端口)
1.提供注册账户
2.根据账户判断用户
"""

import socket
import random
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('192.168.0.103',9001))
dic={}      #使用字典保存每个name对应的字体颜色font_color和背景颜色back_color
while True:
    recv_msg,addr = sk.recvfrom(1024)
    recv_msg=recv_msg.decode('utf-8')
    name=recv_msg.split(':',1)[0]
    if name in dic:
        font_color = dic[name][0]
        back_color = dic[name][1]
    else:
        font_color = random.randint(30, 37)     #随机生成一个字体颜色
        while True:
            back_color = random.randint(40, 47) #随机生成一个背景颜色
            if back_color != font_color + 10:   #确保背景颜色与字体颜色不同
                break
        dic[name]=(font_color,back_color)
    print('\033[1;'+str(font_color)+';'+str(back_color)+'m'+recv_msg+'\033[0m')
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'),addr)








