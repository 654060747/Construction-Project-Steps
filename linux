1、实时跟进硬盘使用情况（watch），-d高亮显示变化区域，-n 1间隔1秒刷新一次
```
watch -d -n 1 df -h(高亮显示每隔1秒变化的情况)
fdisk -l(查看硬盘挂载情况等)
mount /dev/xxx(某硬盘) ./目录(硬盘挂载)
```

2、同时查看多个日志（multitail：sudo apt-get install multitail）
```
multi-tail -f
```

3、程序后台运行（nohup）
```
nohup wget xxx(后台下载xxx)
```

4、xargs(处理换行符、空格,将命令的输出作为参数传递给另一个命令),{}(接收管道给的命令内容与-i配合使用),'-'与-type f/d(f文件,d目录)
```
find . -name '*.jpg' | grep '^-' | wc -l 
find . -type (f|d) -name '*.jpg'| wc -l
ls | grep '^-' | xargs -i mv {} ./目录
ls -R | grep '.bak$' | xargs -i rm ./{daoxiang,hongdeng,yaxian}/{json,xml}/{}(匹配到.bak结尾的数据删除掉)

find . -name '*.jpg' -exec[开始] mv {} ./目录 \;[结束](-exec与xargs -i用法类似，但使用-exec后面需要加上\;)
```

5、演示有无xargs
```
find . -name 0 | ls
find . -mtime 0 | xargs ls(这才是想要的效果)
```

6、-mtime(按天计算)，-[newermt,newerct,newerat](详细时间计算)
```
find . -type f -mtime (...|-1|0|1|2|...) | wc -l
find . -type f -newerct '2019-12-23 09:00' ! -newerct '2019-12-23 15:00' | wc -l
```

7、进程排序,杀进程
```
ps -aux | sort -rnk (4|3)(4按内存使用排序,3按cpu使用排序)
kill -9 xxx(PID)(了解-15与-3区别)
```

8、要使输出内容清晰，可使用制表column -t
```
ls --help | column -t -s:(-s:代表制表以:分割)
```

9.0、cat(顺序显示),tr(字符替换),tac(倒序显示),nl(显示行号类似[cat -n]),head(显示头部),tail(显示尾部),od(二进制显示),less|more(一页一页显示)
```
echo 'LIU' | tr 'IU' 'GE'
cat file | tr 'i' '#' > file(内容字符i替换成字符#)
cat file | tr a-z A-Z > file(大小写转换)
```
9.1、rename文件目录批量命名
```
rename 's/老名字(需要修改的某部分)/新名字/' (*)老名字(*)
rename 's/0/5/g' `grep 0 *0*.jpg`(``用法)
rename 'y/0/5/' *.jpg(跟以上效果一样)
```
9.2、sed(文本内容操作),-i(更改原文件),-n(只输出结果),-i.bak(更改并备份),g(所有)w(写入另一文件)p(打印)d(删除)
```
sed -n '/LIU/,1p' file(匹配文件包含字符LIU所在的行)
sed -i '/LIU/, $ d' file(匹配文件包含首个字符LIU行到文件末尾删除)
sed -i '/LIU/, /GEN/d' file(匹配两个字符包括匹配到的行之间删除)

sed -n 's/\(LIU\)/\1GEN/p' file(正则原子\1引LIU字符)

i(插入)a(添加)c(修改)
sed -i '/LIU/i hello word' file(把hello word插入到匹配到的字符LIU前面)
sed -i '2i hello word' file(第2行插入)
sed -i '/LIU/a hello word' file(添加到字符后)
sed -i '2a hello word' file(第2行添加)
sed -i '/LIU/c GEN' file(含有字符LIU的整行替换成GEN字符)

sed -i '12,14 s/HHH/GGG/g' file(修改文件12到14行)
sed -n 's/HHH/GGG/g;12,14p' file(查看12到14行修改效果)(注意跟上面区别)
sed -ni 's/HHH/GGG/g;12,14p' file(文件内容被修改成12到14行修改过的内容,-ni顺序不能反,可查看相反效果)

sed -i '1,$ d' `grep -rlw liugen .`(精确匹配liugen字符删除文件第一行到末尾内容)
sed -i 's/\+/\&/g' `grep \+ -rl .`(g所有,-r递归目录以下所有,-l列出文件文本内容)
```

10、stat(文件详细信息,比ls -l更加详细),-c(配合%n文件名称、a%权限、%u文件UID、%U用户名、%s/%b大小[字节byte/KB])
```
stat file
stat -c '%n %a %U' file
```

11、export(设置环境变量),env(查看系统所有环境变量)
```
export PATH=$PATH:/home/xxx/xxx/bin
```

12、grep(-v不匹配，-E跟正则(相当egrep)，-i忽略大小写，-c计数，-w精确匹配，-n匹配行，-r递归搜索，-l列表)
```
ipconfig | grep -c IPv4(ip中匹配IPv4计数)
grep -n 'LIU' file(匹配字符LIU在文件第几行)

grep -r 'gen' ./* | grep 'liu'(当前目录下所有文件满足有liu与gen字符)
grep  'gen' ./* | grep 'liu' | grep -v 'ha'(匹配genliu不匹配ha字符)

ls -R . | grep -E '修路|施工' | tr ':' '/' | xargs -i cp -R {} ./ok/(在测试集中寻找修路或者施工的图片复制到ok文件夹)
```

13、dpkg -l(列出ubuntu系统上安装的.deb包)，当要卸载某个模块时不知道版本可使用以下命令
```
sudo dpkg -l | grep -i python(过滤出python安装包)
```

14、awk三剑客老大,[-F指定字符分割默认以空格制表符分割，-v定义变量，NF当前行的字段个数$NF就代表最后一个字段，NR==1打印指定行](awk [options] 'BEGIN{}patten{}END{}' file)，(可以写成脚本文件，如果是纯awk脚本在第一行写成[#!/bin/awk]，类似shell脚本[#!/bin/sh])
```
 awk 'BEGIN{print "姓名 语文 数学 英语"}$2<100{print $1,$2,$3,$4}END{print "总分"}' score.txt | column -t(制表不需要对位)
 awk 'BEGIN{print "姓名 语文 数学 英语"}$2<100{printf "%-5s%-5d%-5d%-5d\n",$1,$2,$3,$4}END{print "总分"}' score.txt(使用的对位不使用制表，printf可以格式化字符串)

awk '/LIU/' file(匹配文件含有LIU字符行)
awk 'NR==2{print $0}' file（打印指定行内容，也可以布尔值NR%2==1奇数行）
cat file | awk '$2=="LIU" {print $0}'(匹配第二列包含字符LIU的行)
echo "LIU GEN" | awk '{ if($1 == "LIU") print $0; else print "nothing"}'（if语句）
ls | awk -F+ '{print $1}'（以+截取取第一列）

sed -i -f sed_shell file(加-i才会修改原文件，-f调用脚本)
awk|sed -f awk_sed_shell(awk|sed脚本语句) file(要处理的文件)
   awk_sed_shell脚本语句格式(只有中间语句部分)：
      BEGIN{print "姓名 语文 数学 英语"}$2<100{print $1,$2,$3,$4}END{print "总分"}
      {print $1}
      或者：
      1iLIU
      $aGEN(第一行插入，最后一行添加)
```

14.1、shuf(随机抽取数据)
```
shuf -n10 1.list > 2.list（先把数据生产1.list再使用shuf随机抽取10行数据到2.list）
```


/etc:配置文件(crontab -e配置同步，/etc/nginx/sites-enabled配置代理ip[使用局域网访问外网]，/etc/network配置网段，/etc/samba配置文件共享，/etc/init.d各种配置开启的地方，/etc/shadow密码记录档案)

免密SSH登录主机：先执行ssh-keygen为当前用户生成公钥，然后执行ssh-copy-id remote-machine

通过SSH挂载远程主机上的文件夹：sshfs name@ip:/远程目录/xx/ /本地目录/xx/，需要安装的软件有FUSE及sshfs；卸载：fusermount -u /本地目录/xx/

递归下载：wget --random-wait -r -p -e robots=off -U Mozilla www.baidu.com（--random-wait等待0.5到1.5秒进行下一次请求，-r递归，-e robots=off忽略robots.txt，-U Mozilla设置User-Agent头为Mozilla，其它：--wait=1h每下载一个文件等1小时）


15、pwd [-P](-P:显示实际路径，非链接[link]路径)

16、mkdir -m 711 目录(-m强制设置属性)，rmdir -p 空目录/空目录/...(递归删除空目录)

17、echo $PATH(显示PATH变量)

18、touch -d '1 days ago' file或者touch -t 1002211325[格式YYMMDDhhmm] sed.txt(创建指定时间的文件，-d按天数，-t按具体时间)

19、umask(查看创建文档的默认属性，-S显示rwx属性)，修改默认属性举例：umask 222(本身、同组group、其它others用户权限都被拿掉了执行w权限)

20、chattr(设置隐藏属性；+i设置档案不能进行任何操作root用户可用，-i取消这种设置；+a|-a档案只能添加数据root用户|取消功能)
21、lsattr(显示隐藏属性；-R递归显示)

22、文件s、t[SBIT]属性(列如:/tmp目录本身权限drwxrwxrwt,在此目录任何人都可以创建、修改文件，但仅有root及创建者才可以删除；/usr/bin/passwd权限-rwsr-xr-x，按道理修改密码只能root有权限，但是用户本身修改自己的密码可以通过s[SUID]获取root权限所以自己也能修改自己的密码；/usr/bin/locate权限-rwx--s--x只能跟此文件同组用户才有s[SGID]权限)

23、which [-a]查找范围最小，只在$PATH路径中搜索，并且只能查找可执行文件；whereis|locate寻找是进入到数据库中的数据而不需要经过硬盘读取寻找，速度快；find功能最强大但速度最慢。

24、!!引用上一条命令，!^|!$引用上一条命令的开头或者结尾，!*引用上一条除了关键字后面所有，!:- 去掉最后一个参数执行上一条命令，![命令]:整数 引用指定命令的第[整数]个,列如:!cp:2引用历史cp命令的第2个参数；history可以查看历史命令，如果需要快速执行某条历史命令只需要!UID，列如：通过history看到历史某条命令id为233，则!233即可快速执行此条命令；![关键字]：列如!find执行上一条的find命令；!?不是关键字?：执行历史包含指定字符的命令； !!:gs/字符a/字符b/替换上一条命令指定字符执行；逻辑非操作[慎用最好不用]：列如rm !(*.jpg)删除不是以jpg结尾的其他文件。

25、du -h(易读方式显示每级目录容量) -a(列出所有的文件目录容量) -s(不列出详细文件目录占用的容量，只显示总量) -sh(易读总量) --max-depth=1参数只显示一级目录统计

26、split -b[指定大小] 100M file(将文件按每个100M拆分,需要指定拆分文件的前缀加在最后面即可，-l[按行拆分])；cat 统一字符* > file(将拆分的文件合并)；diff file1 file2(比较两个文件是否相同)
