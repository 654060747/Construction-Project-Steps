# Windows下django安装环境配置

## 1. 下载安装包

1、Python 下载地址：https://www.python.org/downloads/

2、Django 下载地址：https://www.djangoproject.com/download/

## 2. Python安装

## 3. Django安装

1、下载 Django 压缩包，解压并和Python安装目录放在同一个根目录，进入 Django 目录，执行
```
python setup.py install
```
2、等待安装完成，Django将要被安装到Python的Lib下site-packages

3、配置2个环境变量：C:\Python33\Lib\site-packages\django;C:\Python33\Scripts

## 4. 检查是否安装成功，进入python，执行
```
>>> import django
>>> django.get_version()
```

## 5. 创建helloworld项目，并开启服务
```
django-admin startproject HelloWorld

cd HelloWorld

python manage.py runserver 0.0.0.0:8000
```
## 6. 浏览器访问
```
127.0.0.1:8000
```
