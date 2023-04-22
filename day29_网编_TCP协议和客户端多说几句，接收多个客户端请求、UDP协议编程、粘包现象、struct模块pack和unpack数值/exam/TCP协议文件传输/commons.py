# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: commons.py
# @datatime: 2023/4/22 15:03
import json
import os
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

    @staticmethod
    def json_dump(path: str, obj: object):
        """
        json序列化
        :param path: 序列化对象保存路径
        :param obj:
        :return:
        """
        with open(path, mode='at', encoding='utf-8') as f:
            f.write(json.dumps(obj) + '\n')

    @staticmethod
    def json_load(path: str):
        """
        json反序列化
        :param path:
        :return:
        """
        with open(path, mode='rt', encoding='utf-8') as f:
            try:
                for line in f:
                    yield json.loads(line.strip())
            except EOFError:
                pass

    @classmethod
    def update_fileinfo(cls, path: str, fileinfo: dict):
        """更新db文件信息"""
        filenames = [file['file_name'] for file in Commons.json_load(path)]
        if fileinfo['file_name'] in filenames:
            back_file = os.path.join(os.path.dirname(path), 'backup')
            with open(back_file, mode='wt', encoding='utf-8') as f:
                for info in cls.json_load(path):
                    if info['file_name'] == fileinfo['file_name']:
                        f.write(json.dumps(fileinfo)+'\n')
                    else:
                        f.write(json.dumps(info) + '\n')
                f.close()
            os.remove(path)
            os.rename(back_file, path)
        else:
            Commons.json_dump(path, fileinfo)





if __name__ == '__main__':
    alex = {'name': 'alxe', 'age': 18}
    path = 'db/userinfo'
    # Commons.pickle_dump(path,alex)

    for user in Commons.pickle_load(path):
        print(user)
        print(user['name'])




