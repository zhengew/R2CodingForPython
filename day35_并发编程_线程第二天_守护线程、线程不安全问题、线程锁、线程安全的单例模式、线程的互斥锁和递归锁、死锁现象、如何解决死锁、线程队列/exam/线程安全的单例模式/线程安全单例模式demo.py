# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 线程安全单例模式demo.py
# @datatime: 2023/5/1 10:29

"""
目标:掌握 线程安全的单例模式
"""
class SingleInstance(object):

    from threading import Lock
    __lock = Lock()
    __instance = None
    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
            return cls.__instance
    def __str__(self):
        return '%s' % self.__dict__
class Dog(SingleInstance):
    def __init__(self, name, age):
        self.name = name
        self.age = age
if __name__ == '__main__':
    from threading import Thread, current_thread
    def new_dog(obj, name, age, obj_lst):
        obj_lst.append(obj(name, age))
    t_list = []
    obj_lst = []
    t1 = Thread(target=new_dog, args=(Dog, '小白', 10, obj_lst))
    t2 = Thread(target=new_dog, args=(Dog, '小黑', 15, obj_lst))
    t3 = Thread(target=new_dog, args=(Dog, '花花', 12, obj_lst))
    t1.start()
    t2.start()
    t3.start()
    t_list.append(t1)
    t_list.append(t2)
    t_list.append(t3)
    for t in t_list: t.join()
    for obj in obj_lst: print(obj)




