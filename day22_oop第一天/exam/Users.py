# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/31 07:18
# 文件名称: Users.py

"""
# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
        # 登陆成功之后才创建用户对象
        # 设计一个方法 修改密码
"""

class Users(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def update_pwd(self, new_pwd):
        """
        修改密码
        :param user:
        :return:
        """
        self.password = new_pwd


def login(obj):
    name = input("用户名: ").strip()
    pwd = input("密码: ").strip()
    if name == obj.name and pwd == obj.password:
        return True
    else:
        return False
def main():
    alex = Users('alex', '123456')
    taibai = Users('taibai', '123456')
    if login(alex):
        new_pwd = input("请输入新密码: ")
        alex.password = new_pwd
        print(alex.password)
    else:
        print("用户名或密码错误～")


if __name__ == '__main__':
    main()

