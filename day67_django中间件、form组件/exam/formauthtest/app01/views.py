from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.db import transaction
# form组件
from app01.utils.registerform import RegisterForm

from app01 import models

# Create your views here.

class App01View(View):

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return redirect('login')

        elif request.path == '/login/':

            return render(request, 'login.html')

        elif request.path == '/register/':
            form_obj = RegisterForm()
            return render(request, 'register.html', {'form_obj': form_obj}) # form对象传递给响应对象

    def post(self, request, *args, **kwargs):

        if request.path == '/login/':
            data = request.POST.dict()
            print(data)
            return redirect('register')

        elif request.path == '/register/':
            form_obj = RegisterForm(request.POST)

            print(f'表单数据是否合法：{form_obj.is_valid()}')
            print(f'表单数据字段对象: {form_obj.fields}')

            # 校验数据是否合法
            if form_obj.is_valid():
                data = form_obj.cleaned_data
                del data['r_password']
                # 入库
                with transaction.atomic():
                    models.UserInfo.objects.create(**data)

                print(f'表单校验通过的数据: {form_obj.cleaned_data}')
                return redirect('login')

            else:
                # form表单验证失败
                print(f'表单errors对象: {form_obj.errors}')
                return render(request, 'register.html', {'form_obj': form_obj})
