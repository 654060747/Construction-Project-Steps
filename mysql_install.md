一、下载软件

1. 进入mysql官网，登陆自己的Oracle账号(没有账号的自己注册一个),下载Mysql-5.7.17，下载地址：http://dev.mysql.com/downloads/mysql/

2.将下载好的文件解压到指定目录，解压在E:/mysql-5.7.17-winx64

二、安装过程  

1.首先配置环境变量path，将E:/mysql-5.7.17-winx64/bin配置到自己的path中

环境变量
MySql_HOME===================E:/mysql-5.7.17
Path =========================%MySql_HOME%/bin;

2.在解压路径下复制my-default.ini,修改名称为my.ini如下图所示



3.打开文件my.ini,添加内容如下：

#########################################################

[client]
default-character-set=utf8
[mysqld]
basedir=E:/mysql-5.7.17
datadir=E:/mysql-5.7.17/data
port = 3306
character-set-server=utf8

#########################################################

4.然后将my.ini文件放到bin目录下（一开始我是放在根目录下的，到后面初始化data文件夹的时候一直初始化不了）


三、初始化数据库、配置相关信息

1.以管理员身份运行windows 命令行（特别提醒：WIN7及WIN7以上版本系统这里一定要用管理员身份，不然后续操作会出错）

2. 进入mysql的解压缩目录 D:/mysql-5.7.15-winx64/bin（提醒：此处需要进入bin目录，否则后续操作会出现错误）

3.注册Mysql服务，运行命令：mysqld --install MySQL

如果出现："Service successfully installed.“提示，证明成功安装mysql服务

4.初始化data目录

输入命令：mysqld --initialize-insecure (生成无密码的root用户)

此时在mysql文件夹下会生成一个data文件夹，里面有些文件夹和文件，这样就表明初始化成功了

5.初始化完成后启动mysql服

输入命令：net start mysql

出现MYSQL服务已经启动成功就表示OK

6.设置密码

mysqladmin -u root password 密码

7.开始使用mysql

输入命令：mysql -u root -p

然后输入刚才设置的密码





Navicat连接Mysql8.0.11出现1251错误

在网上查的是,出现这个原因是mysql8 之前的版本中加密规则是mysql_native_password,
而在mysql8之后,加密规则是caching_sha2_password, 解决问题方法有两种,
一种是升级navicat驱动,
一种是把mysql用户登录密码加密规则还原成mysql_native_password.?

?


我常说的是第二种方式?


ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER; #修改加密规则?

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; #更新一下用户的密码?

FLUSH PRIVILEGES; #刷新权限


'root' ? 为你自己定义的用户名


'localhost' 指的是用户开放的IP，可以是'localhost'(仅本机访问，相当于127.0.0.1)，可以是具体的'*.*.*.*'(具体某一IP)，也可以是 '%' (所有IP均可访问)


'password' 是你想使用的用户密码




四、移除

1.如果是移除已安装好正在使用的mysql，则需要先在cmd里面进入到mysql解压目录下的bin目录下，命令行中输入net stop mysql关闭MySQL服务，然后运行命令 mysqld --remove

精彩专题分享：mysql不同版本安装教程 mysql5.7各版本安装教程 mysql5.6各版本安装教程

以上就是本文的全部内容
