"""
内置函数
"""
import logging

# sum
# ret = sum([1, 2, 3, 4, 5], 100) # 115
# print(ret)
#
# # min
# # def func(n: int):
# #     return abs(n)
# #
# # ret = min([11, -3, 5, 7, 11, 2, 12], key=func)
# # print(ret)
#
# # eval
# ret = eval('1+2+3')
# print(ret) # 6
#
# # exec 代码流
# msg = """
# for i in range(10):
#     print(i, end=' ')
# """
#
# exec(msg) # 执行代码 0 1 2 3 4 5 6 7 8 9
#
# # hash
# # print(hash([1, 2])) # TypeError: unhashable type: 'list'
# print(hash('abd')) # -6019060912062306342

# help
# import logging
# help(logging)

# callable 判断一个对象是否可调用
# def func(n: int):
#     return divmod(n, 2)
#
# print(callable(func)) # True
# ret = func(10)
# print(ret)

# int

# print(int(3.6))
#
# # float
# print(float(3))
# print(float(3.12))

# print(complex(1, 30))

# bin oct hex
# print(bin(8)) # 0b1000
# print(oct(8)) # 0o10
# print(hex(8)) # 0x8
#
# # divmod
# ret = divmod(10, 3)
# print(ret) # (3, 1)


# bytes
# s1 = 'test123'
# print(bytes(s1, encoding='utf-8'))
# b = s1.encode('utf-8')
# print(b) # b'test123'
# print(b.decode('utf-8'))
# c = bytes(s1, encoding='utf-8')
# print(c)


# ocr
ret = ord('a')
print(ret) # 97

ret = chr(97)
print(ret) # a


# repr
logger = logging.Logger
print(repr(logger)) # <class 'logging.Logger'>
s1 = 'erwei'
print(repr(s1)) # 'erwei'


# all
ret = all([1, 2, 3, True, False, ''])
print(ret) # False

# any
ret = any([1, 2, 3, True, False, ''])
print(ret) # True

# print
print(1, 2, 3, 4, sep='*', end='\n')

# list
ret = list('abcdefg')
print(ret) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']