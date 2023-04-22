# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: hmac模块_替代hashlib.py
# @datatime: 2023/4/22 14:17

"""
目标:掌握 hmac模块 加盐加密
1.new(key: bytes, msg: bytees, digestmod: 加密算法) 返回值是hmac对象，bytes类型
2.update(msg: bytes): 多次加密
3.digest(): 返回bytes类型的hash值

场景: 在登录验证、校验客户端请求的合法性
"""

import hmac

sat = 'test1' # 随机盐值

h = hmac.new(key=sat.encode('utf-8'), msg='hello'.encode('utf-8'), digestmod='md5')
h.update('world'.encode('utf-8'))
ret = h.digest()  # 返回bytes类型的hash值,长度16
print(ret, type(ret), len(ret)) # b'I\x99\x07^\xc5\x7f\xc9\x82\xe7\x1eA\xb1\x81\xb9XC' <class 'bytes'> 16
ret = h.hexdigest() # 返回str类型的hash值,长度32
print(ret, type(ret), len(ret)) # 4999075ec57fc982e71e41b181b95843 <class 'str'> 32


