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

8.Navicat连接Mysql8.0.11出现1251错误

在网上查的是,出现这个原因是mysql8 之前的版本中加密规则是mysql_native_password,
而在mysql8之后,加密规则是caching_sha2_password, 解决问题方法有两种,
一种是升级navicat驱动,
一种是把mysql用户登录密码加密规则还原成mysql_native_password.?

我常说的是第二种方式?

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER; #修改加密规则?

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; #更新一下用户的密码?

FLUSH PRIVILEGES; #刷新权限

'root' ? 为你自己定义的用户名

'localhost' 指的是用户开放的IP，可以是'localhost'(仅本机访问，相当于127.0.0.1)，可以是具体的'*.*.*.*'(具体某一IP)，也可以是 '%' (所有IP均可访问)

'password' 是你想使用的用户密码

四、移除

1.如果是移除已安装好正在使用的mysql，则需要先在cmd里面进入到mysql解压目录下的bin目录下，命令行中输入net stop mysql关闭MySQL服务，然后运行命令 mysqld --remove

专题分享：mysql不同版本安装教程 mysql5.7各版本安装教程 mysql5.6各版本安装教程

五、mysql基本语句，大小写自己斟酌
遵循规则：select  from  where  group by  having  order by  limit
```
show databases;
drop database 数据库;
use 表
show tables;
create table 表(id int auto_increment primary key,name varchar(20),class varchar(20),yw float(3,2) not null default 0.00,sx float(3,2) not null default 0.00)engine=innodb;(创建表)
INSERT INTO 表( name, class, yw, sx ) VALUES ("x", "xx", x, xx),("x", "xx", x, xx)......;(插入多条数据)
desc 表;(表结构)
truncate table 表;(删除表数据)
drop table 表;
select * from 表;(查询)
```
explain可以清楚看到mysql是如何处理sql语句的，可查看type与Extra的对比
```
explain select * from 表 where 字段 = xxx(不是索引字段);
explain select * from 表 where id = 5(使用主键或者索引字段，查询速度快，详细讲解见印象笔记);
```
mysql 数据库授权（给某个用户授权某个数据库）
```
create user 'liuu'@'%' identified by 'ubuntu';（创建用户：liuu用户，%所有ip也可指定某个ip访问，ubuntu密码）

grant select,insert,update,delete on test.* to 'liuu'@'%';（test.*授权test数据库下的所有表，如果只用*代表所有表）
revoke all on test.* from 'liuu'@'%';（取消授权）
或者
grant select,insert,update,delete on test.* to 'liuu'@'%' identified by 'ubuntu';

注意：grant、revoke是root才有的命令

drop user '用户名'@'IP地址或者%';（删除用户）
rename user '用户名'@'IP地址' to '新用户名'@'IP地址';（修改用户）
set password for '用户名'@'IP地址'=Password('新密码');（修改密码）
```
六、说明：<>内容说明，()语句中真实存在，[]可选语句，|选其一

1.数据表创建外键<关联字段的数据类型必须匹配>：constraint 外键名<随便取> foreign key(某个字段作为外键) references  主表名(主表要关联的字段)

2.字段名 数据类型 primary key<创建主键，唯一性不能为空>
   字段名 数据类型 not null<非空约束，不能为空>

3.字段名 数据类型 unique<唯一，可以为空且可以多个字段>
   字段名 数据类型 default 默认值<默认约束，指定默认值>
   字段名 数据类型 auto_increment<自增>

4.查看表结构：describe 表名；或者 desc 表名;
   show create table 表名 \G<查看表的详细结构语句，\G显示结果易于查看不混乱>

5.修改表名：alter table 旧表名 rename 新表名; 

   修改字段数据类型：alter table 表名 modify 字段名 新数据类型; 
   
   修改字段名：alter table 表名 change 旧字段名 新字段名 新数据类型; <change同样可以实现modify效果>
   
   添加字段：alter table 表名 add 新字段名 数据类型 [条件约束,列如：not null] [first|after 已有字段名]<添加到已有字段名后，如不指定默认添加到末尾>;
   
   删除字段：alter table 表名 drop 字段名;
   
   删除外键：alter table 表名 drop foreign key 外键名<constraint定义的外键名>;

6.abs(x)：x的绝对值；pi()：圆周率π；sqrt(x)：x的二次方根；mod(x,y)：x除以y后的余数；ceil(x)：向上取值；floor(x)：向下取值；round(x)：四舍五入取值；round(x,y)：保留y位小数点并四舍五入取值；
