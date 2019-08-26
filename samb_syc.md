sudo nano /etc/samba/smb.conf 
sudo service smbd restart
 sudo nano /etc/nginx/sites-enabled/new
sudo service nginx restart
df -h
sudo mkdir 03.xxx
sudo mount /dev/sde1 /03.xxx
crontab -e
sudo service cron restart
history



00 13 * * * rsync --remove-source-files -av 用户名@ip:/home/xxx/xx/ ./xxx/xxx  每天一点同步数据
