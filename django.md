# Windows下django安装环境配置

## 下载安装包

1、Python 下载地址：https://www.python.org/downloads/

2、Django 下载地址：https://www.djangoproject.com/download/

## Python安装

## Django安装

1、下载 Django 压缩包，解压并和Python安装目录放在同一个根目录，进入 Django 目录，执行
```
python setup.py install
```
2、等待安装完成，Django将要被安装到Python的Lib下site-packages

3、配置2个环境变量：C:\Python33\Lib\site-packages\django;C:\Python33\Scripts

## 检查是否安装成功，进入python，执行
```
>>> import django
>>> django.get_version()
```

## 创建helloworld项目，并开启服务
```
django-admin startproject HelloWorld

cd HelloWorld

python manage.py runserver 0.0.0.0:8000
```
## 浏览器访问
```
127.0.0.1:8000
```
## 模板配置
1、 manage.py同级目录创建templates目录，并创建runoob.html，目录用来放html文件

2、修改 TEMPLATES 中的 DIRS 为 [BASE_DIR / "templates"]
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # 要修改的位置
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
3、修改view.py，向模板提交数据，用来操作html模板
```
from django.shortcuts import render
 
def runoob(request):
    context = {}
    context['hello'] = 'Hello!!!'
    context['world'] = 'World!!!'
    return render(request, 'runoob.html', context)
```
4、修改重定向urls.py：
```
from django.urls import path
from . import view
 
urlpatterns = [
    path('runoob/', view.runoob),
]
```
5、runoob.html数据接收，也可使用过滤器管道输出，更多过滤用法自行查看
```
<h1>{{ hello }}</h1>
<strong>{{ world }}</strong>
# 接收的数据通过|过滤变小写
<p>{{ {{ hello|lower }} }}</p>
```
## ORM（mysql配置）
1、安装MySQL

2、创建 MySQL 数据库( ORM 无法操作到数据库级别，只能操作到数据表)语法：
```
create database runoob(数据库名称) default charset=utf8; # 防止编码问题，指定为 utf8
```
3、在项目的 settings.py 文件中找到 DATABASES 配置项，中文注释，settings.py 文件头部添加 # -*- coding: UTF-8 -*-
```
DATABASES = { 
    'default': 
    { 
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'xxx', # 数据库名称
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
        'PORT': 3306, # 端口 
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'xxx', # 数据库密码
    }  
}
```
4、告诉 Django 使用 pymysql 模块连接 mysql 数据库：
```
# 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
import pymysql
pymysql.install_as_MySQLdb()
```
## ORM（定义模型）
1、创建 APP，与manage.py同级目录
```
django-admin startapp TestModel
```
2、修改 TestModel/models.py 文件，数据类型CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度
```
# models.py
from django.db import models
# 类名Test即为表名，且继承models.Model，表名组成结构为：应用名_类名（如：testmodel_test）
class Test(models.Model):
    name = models.CharField(max_length=20)
```
3、settings.py 中找到INSTALLED_APPS添加app
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',               # 添加此项
)
```
4、常见报错信息
> 报错django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3. 原因：django2.2和pymysql版本不匹配。mysqldb不支持python3，\Python37\Lib\site-packages\django\db\backends\mysql（python安装目录）打开base.py，注释掉以下内容：
```
if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
``` 
> \Python37\lib\site-packages\django\db\backends\mysql\operations.py”, line 146，last_executed_query方法里的decode修改为encode

5、报错解决运行命令：
```
python manage.py migrate   # 创建表结构

python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate TestModel   # 创建表结构
```
## ORM（数据库操作）
#### 增
1、settings同级目录中添加testdb.py文件，用来操作数据库(view.py操作html)，添加内容：
```
# -*- coding: utf-8 -*-
from django.http import HttpResponse 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    # 相当于sql的Insert
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
```
2、修改重定向urls.py：
```
from django.urls import path
from . import testdb

urlpatterns = [
    path('testdb/', testdb.testdb),
]
```
3、测试访问 http://127.0.0.1:8000/testdb 就可以看到数据添加成功的提示
#### 删
#### 改
#### 查
