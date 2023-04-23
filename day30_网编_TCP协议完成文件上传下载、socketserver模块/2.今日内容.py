# 0.tcp协议的自定义协议解决粘包问题 主要掌握逻辑和代码
    # 1 recv(1024)不代表一定收到1024个字节,而是最多只能收这么多
    # 2 两条连续发送的数据一定要避免粘包问题
    # 3 先发送数据的长度 再发送数据
    #   发送的数据相关的内容组成json:先发json的长度,再发json,json中存了接下来要发送的数据长度,再发数据
# 1.验证客户端合法性
    # 1 什么场景用
    # 2 什么逻辑 什么是密钥 为什么要发送随机的字符串 使用什么算法呀? 算法有什么要求?
    # 3 代码 怎么实现的? hashlib hmac
# 2.并发的tcp协议server端 -- socketserver
    # 1.会背
    # 2.知道代码从哪儿开始 当客户端来链接的时候直接和handle中的代码交互self.request == conn

import os
os.urandom()