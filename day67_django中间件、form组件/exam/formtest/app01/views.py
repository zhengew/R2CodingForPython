from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django import forms # form 组件

from app01 import models

# Create your views here.

class LoginForm(forms.Form):

    # 文本框
    name = forms.CharField(
        label='用户名',
        initial='大臂哥',
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
    )
    # 密码框
    password = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
    )

    # 单选按钮
    sex = forms.ChoiceField(
        label='性别',
        choices=((1, '男'), (2, '女'), (3, '保密'),),
        initial=3,
        widget=forms.widgets.RadioSelect(),
    )

    # 下拉选择框
    city = forms.ChoiceField(
        label='城市',
        choices=((1, '北京'), (2, '上海'), (3, '广州'),),
        initial=1,
        widget=forms.widgets.Select(),
    )

    # 多选复选框
    hoby = forms.MultipleChoiceField(
        label='爱好',
        choices=((1, '抽烟'), (2, '喝酒'), (3, '烫头'),),

        widget=forms.widgets.CheckboxSelectMultiple(),
    )

    # 多选下拉选择框
    girls = forms.MultipleChoiceField(
        label='女朋友',
        choices=((1, '红旭妹妹'), (2, '雪飞姐姐'), (3, '详细哥哥'),),
        widget=forms.widgets.SelectMultiple(),
    )

    # 单选 checkbox
    status = forms.ChoiceField(
        label='remeber me',
        initial=True, # 默认勾选
        choices=(('True', '红旭妹妹'), ('False', '雪飞姐姐')),
        widget=forms.widgets.CheckboxInput,
    )

    # 日期
    birthday = forms.CharField(
        label='生日',
        widget=forms.widgets.TextInput(attrs={'type': 'Date'}),
    )


def index(request, *args, **kwargs):

    if request.method == 'GET':
        return redirect('register')

def register(request, *args, **kwargs):

    form_obj = LoginForm()

    if request.method == 'GET':
        return render(request, 'register.html', {'form_Obj': form_obj,})

    elif request.method == 'POST':

        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        print(uname, pwd)
        if uname == 'zew' and pwd == '123456':
            ret = {"RETCODE": 200, "RETMSG": "success"}
            return JsonResponse(ret)
        else:
            ret = {"RETCODE": "USERNAME_OR_PASSWORD_ERROR", "RETMSG": "用户名或密码错误"}
            return JsonResponse(ret)