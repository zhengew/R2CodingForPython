# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/24 21:42
# 文件名称: filter_demo.py

l1 = ['1', '20', '', '', '30']
ret = filter(lambda n:n, l1) # 列表去除空
print(list(ret)) # ['1', '20', '30']

