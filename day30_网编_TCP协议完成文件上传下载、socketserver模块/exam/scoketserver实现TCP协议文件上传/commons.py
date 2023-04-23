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
            f.write(json.dumps(obj, ensure_ascii=False) + '\n')

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
                        f.write(json.dumps(fileinfo, ensure_ascii=False)+'\n')
                    else:
                        f.write(json.dumps(info, ensure_ascii=False) + '\n')
                f.close()
            os.remove(path)
            os.rename(back_file, path)
        else:
            Commons.json_dump(path, fileinfo)

    @classmethod
    def get_dbfiles_info(cls, path: str):
        """
        读取服务端存储的文件信息
        :param path: ./db/fileinfo
        :return: 文件信息列表:[{"file_name": "我的自学编程之路.pdf", "size": 33143, "md5_value": "7a571a0fed4dae6b4174e9a23a5970ff"}, ...]
        """
        return sorted([file for file in cls.json_load(path)], key=lambda x: x['file_name'])



if __name__ == '__main__':
    alex = {'name': 'alxe', 'age': 18}
    path = 'db/userinfo'
    # Commons.pickle_dump(path,alex)
    '''
    /home/zew/WeChatFiles/files/我的自学编程之路.pdf
    /home/zew/WeChatFiles/files/8、债券交易用户故事2022-01-30.docx
    '''
    # for user in Commons.pickle_load(path):
    #     print(user)
    #     print(user['name'])

    path = r'./db/fileinfo'
    ret = Commons.get_dbfiles_info(path)
    print(ret)


