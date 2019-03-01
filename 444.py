# coding=utf-8
import requests
import random
from bs4 import BeautifulSoup
import pyquery
import re



# ua = UserAgent()
# User_Agent = ua.random

url = 'http://www.dianping.com/shop/27227334'

headers = {
		'Referer':url,
        'Host':'www.dianping.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'
     }
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
html = resp.text

# css_url_regex = re.compile(r'href="//(s3plus.meituan.net.*?)\"')
# css_url = re.search(css_url_regex, html).group(1)
# css_url = 'http://' + css_url
css_url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/5de9a9098d8d30d7d65f16ab93871bb4.css'

# 获取css文件
css_resp = requests.get(css_url)
# regex_kj_svg = re.compile(r'e\[class\^="tf"\][\s\S]*?url\((.*?)\)')
css_html = css_resp.content.decode('utf-8')

# 提取svg图片的url
# svg_kj_url = re.search(regex_kj_svg, css_html).group(1)
# svg_kj_url = 'http:' + svg_kj_url
svg_kj_url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/48c69de6720605cffb96fec58b383f5e.svg'

# 获取表示数字的svg文件
svg_kj_resp = requests.get(svg_kj_url)
svg_kj_html = svg_kj_resp.text
# 匹配出svg图片的10个数字
number = re.search(r'\d{42}', svg_kj_html).group()
# number = '517502868063750541820128609368979844350964180396761267454657729825260709221835817009942281193743637379245341065513471645061898723015173934980432529486'

# 匹配出以kj-开头的class属性
regex_kjs_css = re.compile(r'\.(tf\w{3})[\s\S]*?-(\d+)')
kjs = re.findall(regex_kjs_css, css_html)
# for x in kjs:
# 	print(x)
kjs = {i[0]:int(i[1]) for i in kjs}
# 根据偏移量排序
temp = sorted(kjs.items(), key=lambda x:x[1])
# 将class属性与其表示的数字组成字典
kjs = {temp[i][0]:number[i] for i in range(len(number))}
print(kjs)
# pyquery对象
doc = pyquery.PyQuery(html)
# 先拿出评论的HTML，在用正则匹配
regex = r'tf\w{3}'
review_html = doc('#basic-info > div.expand-info.address').html()
temp = re.findall(regex, review_html)
print(temp)
# 将匹配出的结果的class属性替换为相应的数字
for n,i in enumerate(temp):
    if i != '1':
        temp[n] = kjs[i]
# 拼接结果，转化为整型数字
review = int(''.join(temp))
print('地址：', review)
