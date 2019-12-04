# 输入git clone 粘贴你复制的链接（远程地址）
```
git clone https://github.xxxxxxx
```

```
cd demo 
git status 
git add --all
git commit -m"1"
```
# （首次上传GitHub，不是首次上传无视本步骤）接着输入
```
git config --global user.email "自己的邮箱"
git config --global user.name "用户名"
```

```
git push  
```

# 删除a目录下的2.txt文件   删除a目录git rm -r --cached a
```
git rm -r --cached a/2.txt 
git commit -m "删除a目录下的2.txt文件" 
git push
```

# 如果远程分支被省略，如上则表示将本地分支推送到与之存在追踪关系的远程分支（通常两者同名），如果该远程分支不存在，则会被新建
```
git push origin master
```

# 如果当前分支只有一个远程分支，那么主机名都可以省略，形如 git push，可以使用git branch -r ，查看远程的分支名
```
git push
```

# git要强制覆盖，那么可以使用--force命令
# 如果远程主机的版本比本地版本更新，推送时Git会报错，要求先在本地做git pull合并差异，然后再推送到远程主机。这时，如果你一定要推送，可以使用–force选项。
```
git push --force origin master
```

# 查看远程仓库
```
git remote -v
```
# 删除远程仓库
```
git remote remove origin
```
# 添加远程仓库
```
git remote add origin 仓库地址(https://github.com/654060747/Reptile_pbs.git)
```
