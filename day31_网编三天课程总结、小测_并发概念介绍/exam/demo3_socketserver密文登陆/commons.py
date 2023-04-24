# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: commons.py
# @datatime: 2023/4/24 下午3:40
import hmac
import json
class Commons(object):
    """
    服务端公共组件
    """
    @classmethod
    def save_users(cls, path:str, obj: object):
        """
        保存用户信息
        :param path: 序列化对象存储路径
        :param obj:
        :return:
        """
        with open(path, mode='at', encoding='utf-8') as f:
            f.write(json.dumps(obj, ensure_ascii='utf-8') + '\n')
        f.close()
    @classmethod
    def get_all_users(cls, path:str):
        """
        获取已注册用户信息
        :param path:
        :return:
        """
        with open(path, mode='rt', encoding='utf-8') as f:
            for user in f:
                yield json.loads(user.strip())
    @classmethod
    def get_md5(cls, private_key:str, login_pwd:str):
        """
        公钥私钥加密
        :param private_key:
        :param login_pwd:
        :return:
        """
        h = hmac.new(key=public_key.encode('utf-8'), msg=private_key.encode('utf-8')
        return h.hexdigest()

if __name__ == '__main__':
    path = r'userinfo'
    # alex = {'name': 'alex', 'pwd': 'c45c484aea5abb4dd212961d5bc44164'}
    # Commons.save_users(path, alex)

    users = [user for user in Commons.get_all_users(path)]
    print(users)
