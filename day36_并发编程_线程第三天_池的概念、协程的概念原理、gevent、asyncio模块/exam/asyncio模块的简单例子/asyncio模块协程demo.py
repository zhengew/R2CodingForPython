# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: asyncio模块协程demo.py
# @datatime: 2023/5/3 17:09

"""
目标:演示通过asyncio模块实现协程
"""
import asyncio
import time

async def func(name):
    print(time.time(), ':start', name)
    # await 可能会发生阻塞的方法
    # await 关键字必须写在 async声明的函数里
    await asyncio.sleep(1) # 模拟遇到阻塞事件
    print(time.time(), ':end')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([func('alex'), func('taibai'), func('大壮')]))




