"""
URL configuration for urltest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from root import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home), # root视图，项目登录页
    path('home/', views.index), # 登录成功后，重定向跳转到 home.html
    path('app01/', include('app01.urls')), # path第一个参数是应用名，include通过 '应用名.urls'路由，跳转到应用下的视图
    path('app02/', include('app02.urls')),
]
