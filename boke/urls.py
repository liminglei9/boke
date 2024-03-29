"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',views.index),
    path('index/',views.index),
    path('about/',views.about),
    path('listpic/',views.listpic),
    path('newslistpic/',views.newslistpic),
    re_path('newslistpic/(?P<page>\d+)',views.newslistpic),
    path('base/',views.base),
    path('app/',include('bokeapp.urls')),
    re_path('articlecontext/(?P<id>\d+)',views.articlecontext),
    path('adddata/',views.adddata),
    path('ckeditor/',include('ckeditor_uploader.urls'))
]
