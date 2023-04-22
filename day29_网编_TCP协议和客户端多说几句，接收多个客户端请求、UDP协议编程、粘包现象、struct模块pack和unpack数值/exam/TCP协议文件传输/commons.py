# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: commons.py
# @datatime: 2023/4/22 15:03

import pickle
class Commons(object):

    """
    文件上传服务端的公共组件
    """
    @staticmethod
    def pickle_dump(path: str, obj: object):
        with open(path, mode='ab') as f:
            pickle.dump(obj, f)

    @staticmethod
    def pickle_load(path: str):
        with open(path, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break



if __name__ == '__main__':
    alex = {'name': 'alxe', 'age': 18}
    path = 'db/userinfo'
    # Commons.pickle_dump(path,alex)

    for user in Commons.pickle_load(path):
        print(user)
        print(user['name'])




