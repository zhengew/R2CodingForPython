# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: libControl.py
# @datatime: 2023/9/7 23:08

import hashlib

def get_md5(sat: str, data: str):

    md5_hash =  hashlib.md5(sat.encode('utf-8'))
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()