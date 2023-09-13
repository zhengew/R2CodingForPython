import re

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django import forms # form 组件
from django.core.validators import RegexValidator # 字眼校验验证器
from django.core.exceptions import ValidationError # 校验错误信息

from app01 import models
# Create your views here.

# 自定义校验函数
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  #自定义验证规则的时候，如果不符合你的规则，需要自己发起错误

class LoginForm(forms.Form):


    # 文本框
    name = forms.CharField(
        required=True, # 默认必输
        min_length=6,
        label='用户名',
        initial='大臂哥',
        help_text='这是输入用户名的地方，不能为空，最小6位字符',
        # validators=[RegexValidator(r'^金瓶梅', '没看过不能通过'), RegexValidator(r'红旭妹妹$', '没看过红旭妹妹不能通过'),],

        # validators=[mobile_validate], # 自定义校验函数

        error_messages={
            'required': '不能为空',
            'min_length': '不能太短',
        },
        # widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        widget=forms.widgets.TextInput,
    )
    # 密码框
    password = forms.CharField(
        min_length=8,
        max_length=10,
        label='密码',
        # widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
        widget=forms.widgets.PasswordInput,
    )

    # 确认密码
    r_password = forms.CharField(
        min_length=8,
        max_length=10,
        label='确认密码',
        # widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
        widget=forms.widgets.PasswordInput,
    )


    # # 单选按钮
    # sex = forms.ChoiceField(
    #     label='性别',
    #     choices=((1, '男'), (2, '女'), (3, '保密'),),
    #     initial=3,
    #     widget=forms.widgets.RadioSelect(),
    # )
    #
    # # 下拉选择框
    # city = forms.ChoiceField(
    #     label='城市',
    #     choices=((1, '北京'), (2, '上海'), (3, '广州'),),
    #     initial=1,
    #     widget=forms.widgets.Select(),
    # )
    #
    # # 多选复选框
    # hoby = forms.MultipleChoiceField(
    #     label='爱好',
    #     choices=((1, '抽烟'), (2, '喝酒'), (3, '烫头'),),
    #
    #     widget=forms.widgets.CheckboxSelectMultiple(),
    # )
    #
    # # 多选下拉选择框
    # girls = forms.MultipleChoiceField(
    #     label='女朋友',
    #     choices=((1, '红旭妹妹'), (2, '雪飞姐姐'), (3, '详细哥哥'),),
    #     widget=forms.widgets.SelectMultiple(),
    # )
    #
    # # 单选 checkbox
    # status = forms.ChoiceField(
    #     label='remeber me',
    #     initial=True, # 默认勾选
    #     choices=(('True', '红旭妹妹'), ('False', '雪飞姐姐')),
    #     widget=forms.widgets.CheckboxInput,
    # )
    #
    # # 日期
    # birthday = forms.CharField(
    #     label='生日',
    #     widget=forms.widgets.TextInput(attrs={'type': 'Date'}),
    # )

    # 演示 Hook 钩子
    # 1. 局部狗子  clean_字段名称
    def clean_name(self):
        value = self.cleaned_data['name']
        if 'zew' in value:
            raise ValidationError('含有敏感词汇zew')
        else:
            return value

    # 2. 全局钩子
    def clean(self):
        # 程序能走到该函数,前面校验已经通过了,所以可以从cleaned_data中取出密码和确认密码
        # 字段校验通过以后才会走全局钩子
        value = self.cleaned_data
        print(f'value: {value}')
        p1 = value.get('password', None)
        p2 = value.get('r_password', None)
        if p1 == p2:
            return value
        else:
            self.add_error('r_password', '两次输入密码不一致！！') # 错误信息添加到 errors 对象里
            raise ValidationError('两次输入的密码不一致 ')

# 视图函数
def index(request, *args, **kwargs):

    if request.method == 'GET':
        return redirect('register')

def register(request, *args, **kwargs):

    form_obj = LoginForm()

    if request.method == 'GET':
        return render(request, 'register.html', {'form_obj': form_obj,})

    elif request.method == 'POST':

        # uname = request.POST.get('username')
        # pwd = request.POST.get('password')
        #
        # print(uname, pwd)
        # if uname == 'zew' and pwd == '123456':
        #     ret = {"RETCODE": 200, "RETMSG": "success"}
        #     return JsonResponse(ret)
        # else:
        #     ret = {"RETCODE": "USERNAME_OR_PASSWORD_ERROR", "RETMSG": "用户名或密码错误"}
        #     return JsonResponse(ret)

        # 演示 form 验证
        form_obj = LoginForm(request.POST)
        print(form_obj.is_valid())
        print(form_obj.fields)
        if form_obj.is_valid():  # 校验数据是否合法
            print('true')
            print(form_obj.cleaned_data)  # 通过校验的数据
            return HttpResponse('200 ok')
        else:
            print('false')
            print(form_obj.errors)
            return render(request, 'register.html', {'form_obj': form_obj})

