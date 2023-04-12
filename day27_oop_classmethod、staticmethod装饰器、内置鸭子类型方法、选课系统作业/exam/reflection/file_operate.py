# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: file_operate.py
# @datatime: 2023/4/12 07:19

"""
# 用反射完成
# python xx.py cp path1 path2
# python xx.py rm path
# python xx,py mv path1 path2
"""
import os
import sys
import shutil
import time


class FileOper(object):
    @staticmethod
    def cp(path1: str, path2: str):
        """拷贝文件"""
        if os.path.exists(path1) and os.path.exists(path2):
            shutil.copy2(path1, path2)
    @staticmethod
    def rm(path: str):
        """删除文件或目录"""
        if os.path.isfile(path):
            print(111)
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)

    @staticmethod
    def mv(path1: str, path2: str):
        """移动文件或目录，如果存在则判断是否覆盖"""
        if os.path.exists(path1) and os.path.exists(path2):
            filename = os.path.basename(path1)
            if filename in next(os.walk(path2))[2]:
                command = input(f"{path2}中已存在文件{filename}, 是否覆盖? Y/N")
                if command.upper() == 'Y':
                    abspath = os.path.join(path2, filename)
                    FileOper.rm(abspath)
                    shutil.move(path1, path2)
                elif command.upper() == 'N':
                    print(f"取消移动文件:{filename}至{path2}~")
            else:
                shutil.move(path1, path2)

def run():
    """
    在主方法中进行脚本操作
    :return:
    """
    pass


if __name__ == '__main__':
    FileOper.cp(r'file_operate.py', 'a')
    f = open('a/test1', mode='w', encoding='utf-8')
    f.close()

    # os.remove('test1')
    FileOper.rm('a/test1')

    f = open('a/test3', mode='w', encoding='utf-8')
    f.close()
    FileOper.mv('a/test3', 'b')



