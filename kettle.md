#  Windows kettle(ETL)安装

## 下载安装包

1、kettle 下载地址：https://sourceforge.net/projects/pentaho/files/Data%20Integration/

2、Java下载安装

## 环境配置

1、Java、kettle环境配置：

JAVA_HOME：D:\Program Files\Java\jdk1.7.0_25（安装jdk路径）

CLASSPATH：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar

Path：在path路径中添加%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;

KETTLE_HOME：D:\Program Files\data-integration(安装kettle路径)
```
注意：kettle 7.0以上版本使用java 8,该版本kettle对应jdk1.8 (使用java 14版本不兼容)
```

## 闪退问题解决

1、双击spoon.bat后一闪就没了，修改一下spoon.bat里内存配置：
```
if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms2058m" "-Xmx1024m" "-XX:MaxPermSize=256m"

改为

if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms512m" "-Xmx512m" "-XX:MaxPermSize=256m"

修改之后保存，重新启动spoon.bat即可解决问题。
```

## 连接mysql数据库

1、报以下错误，是你没有下载mysql 的jdbc驱动jar包，
```
Driver class 'org.gjt.mm.mysql.Driver' could not be found, make sure the 'MySQL' driver (jar file) is installed.
org.gjt.mm.mysql.Driver
```
2、jar包下载地址：https://dev.mysql.com/downloads/connector/j/；下载jar包后， 还要看jar包下是否有org.gjt.mm.mysql该路径下的 Driver.class文件

3、以下两个jar包下均有这个org.gjt.mm.mysql路径，所以选择任意一个jar包，然后放在kettle的安装路径xxx\data-integration\lib 文件夹重启kettle
```
mysql-connector-java-5.1.49.jar
mysql-connector-java-5.1.49-bin.jar
```
