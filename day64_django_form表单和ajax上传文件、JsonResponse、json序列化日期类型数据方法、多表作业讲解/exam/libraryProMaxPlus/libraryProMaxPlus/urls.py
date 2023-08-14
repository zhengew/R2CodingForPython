"""
URL configuration for libraryProMaxPlus project.

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
from django.urls import path
from root import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 登录
    path('', views.RootView.as_view(), name='login'),
    # 查看书籍
    path('showBooks/', views.RootView.as_view(), name='showBooks'),
    # 添加书籍
    path('addBook/', views.RootView.as_view(), name='addBook'),
    # 编辑书籍
    path('editBook/<int:id>/', views.RootView.as_view(), name='editBook'),
    # 删除书籍
    path('delBook/<int:id>/', views.RootView.as_view(), name='delBook'),
]
