# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: loginform.py
# @datatime: 2023/9/26 07:05

from django import forms # form组件
from django.core.validators import RegexValidator # 字段正则校验
from django.core.exceptions import ValidationError # 校验错误

from app01 import models # 模型表

class RegisterForm(forms.Form):

    # 文本框
    username = forms.CharField(
        required=True, # 默认必输，非必输显示的改为False
        min_length=3,
        max_length=16,
        label='用户名',
        # initial='test1',
        help_text='用户名限制3～16个字符，不能为空',
        error_messages={
            'required': '用户名不能为空',
            'min_length': '长度不能低于3位',
            'max_length': '长度不能大于16位',
        },
        widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}),
    )

    # 密码框
    password = forms.CharField(
        required=True, # 必输
        min_length=6,
        max_length=16,
        label='密码',
        error_messages={
          'required': '密码不能为空',
          'min_length': '长度不能低于6位',
          'max_length': '长度不能大于16位',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}),
    )

    # 确认密码
    r_password = forms.CharField(
        required=True,
        min_length=6,
        max_length=16,
        label='确认密码',
        error_messages={
          'required': '确认密码不能为空',
          'min_length': '长度不能低于6位',
          'max_length': '长度不能大于16位',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入确认密码'}),
    )

    # 演示 hook 钩子
    # 1. 局部钩子 方法名： clean_字段名
    def clean_username(self):
        uname = self.cleaned_data.get('username')

        # 用户已注册，则主动抛异常 ValidationError, 否则 return 字段值
        if models.UserInfo.objects.filter(username=uname).exists():
            raise ValidationError(f'该用户已注册:{uname}')
        else:
            return uname

    # 2. 全局钩子
    def clean(self):
        # 程序能走到该函数，说明前面校验已经通过了，所以可以从cleaned_data中取密码和确认密码
        # 字段校验通过以后才会走全局钩子
        data = self.cleaned_data
        print(f'表单校验通过的数据:{data}')
        password = data.get('password', None)
        r_password = data.get('r_password', None)
        if password == r_password:
            return data
        else:
            # 错误信息添加到 errors 对象中，并指定一个字段接收错误信息
            self.add_error('r_password', '两次输入密码不一致')
            self.add_error('password', '两次输入密码不一致')
            # 全局钩子也要主动抛异常
            raise ValidationError('两次输入的密码不一致')
