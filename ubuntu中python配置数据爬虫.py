# codeing:utf-8
#下载python => https://www.python.org/downloads/
# 1.下载谷歌浏览器并安装 => http://www.ubuntuchrome.com/
# 2.下载谷歌驱chromedriever => https://chromedriver.storage.googleapis.com/index.html
# 3.把下载的chromedriver放到/usr/local/bin/ => sudo mv chromedriver /usr/local/bin/  3.01：windows下放入谷歌浏览器的Application目录下，
#   并把此目录添加到环境变量path中
# 4.安装python,再安装selenium => pip install selenium
# 5.打开pythonIDLE测试环境是否配置成功 => from selenium import webdriver;browser = webdriver.Chrome();browser.get("http://www.baidu.com")
# 6.pip install bs4 pyquery selenium -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com
# 7.注意可能会有pip与pip3区别

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import re
from pyquery import PyQuery as pq
import csv
from bs4 import BeautifulSoup

browser = webdriver.Chrome()  # 打开浏览器

def view_name(i):
	
	url = 'http://zhao.resgain.net/name_list_' + str(i) + '.html'

	browser.get(url)  # 进入相关网站

	html = browser.page_source  # 获取网站源码
	data = str(pq(html))  # str() 函数将对象转化为适于人阅读的形式。
		#print(data)
	data = BeautifulSoup(data)

	# 先找到class属性对应的div
	name_all = data.find_all('div',{'class':'col-xs-12'})

	for div in name_all:

		# 在div下找到class属性对应的a标签
		ass = div.find_all('a',{'class':'btn btn-link'})

		# print(len(ass))
		if len(ass)>0:
			# print(ass[0].getText())
			for name_list in ass:

				name = name_list.getText()

				print(name)
	pass

for i in range(1,11):
	
	# print(i)

	view_name(i)
