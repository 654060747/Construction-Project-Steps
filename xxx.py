# coding=utf-8
import requests
import time, json, os
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
# from tomorrow import threads
# import random
# 引入模块
# from RestApi import RestApi
# from daili import new_ip, del_ip

# 初始化
# api = RestApi()

#  创建处理记录
#  api.create_record(name)
#    传入参数:
#         name:  2018-04-09 晴 上午
#     返回参数 : 14
s_id = 100000000
e_id = 100000050

def create_user_with_photos(data):
	try:
		api.create_user_with_photos(data)
	except Exception as e:
		print (" api request fail 	. 	.		. ", format(e)) # 接口请求失败

##### 参数必须在上面定义
# @threads(20)

def write_file(data_list):

	file_name = file_name_load+"/68521782/"+"xxx.csv"
	with open(file_name, 'a+', encoding='gbk') as f:
		writer = f.write(data_list+'\n')

file_name_load = "./download"
def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

# @threads(5)
# def check_html(data, sn):
# 	try:
# 		nav_text = data.find_all('ul', class_="nav_l")[0]
# 		photo_text = nav_text.find_all('li')[1]
# 		photo_title = photo_text.text
# 		photo_lik=photo_text.find('a').get("href")

# 		# print(photo_title)
# 		# print(photo_lik)
# 		try:
# 			if "的照片" in photo_title:
# 				num = int(photo_title.split('(')[1].strip(")"))
# 				if num > 2 :
# 					data = str(num) + "," + str(sn)  + "," + photo_lik
# 					# print (num)
# 					photo_hash = photo_lik.split('uid_hash=')[1].split('&')[0]
# 					# http://photo.jiayuan.com/showphoto.php?uid_hash=97513ed75d4ee0b49977540cc28adeea&tid=0&cache_key=
# 					#调用接口
# 					# print( sn + "========================================")
# 					# photos
# 					photos = ['1', "2", "2"]

# 					d = {'uid': sn, 'photo_num': num, 'photo_hash': photo_hash, 'sign': 2, photos: photos }
# 					create_user_with_photos(d)

# 					# #写文件
# 					# write_file(data)
# 		except Exception as e:
# 			print ("no photo.		. 	. 	.		. ", format(e)) # 没有照片
# 	except Exception as e:
# 		print(" x		.		. 	. 	x", format(e))  # 账户已关闭

def function():

	url="https://www.tianyancha.com/company/68521782"

	CheckDir(file_name_load+"/68521782/")

	s=requests.session()
	headers={

	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Host':'www.tianyancha.com',
	'Referer':'https://www.tianyancha.com/',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2864.400',
	'X-Requested-With':'XMLHttpRequest',

    }

	cookies={
	'aliyungf_tc':'AQAAAOLw6mVPhQkALrbrdBZAB+ApUu4b',
	'csrfToken':'XWa9-N9stSNoHagGugqWpVZn',
	'TYCID':'e41e6c502eb811e982cbc392d8a84c8f',
	'undefined':'e41e6c502eb811e982cbc392d8a84c8f',
	'ssuid':'3855799584',
	'_ga':'GA1.2.678265784.1549970952',
	'_gid':'GA1.2.1653442593.1549970952',
	'RTYCID':'d4ca626473f8440e82e251a87c8913a0',
	'CT_TYCID':'fa16f903a9854218b2faca9fc7d1da8c',
	'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1549970952,1549971171',
	'__insp_wid':'677961980',
	'__insp_nv':'true',
	'__insp_targlpu':'aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY29tcGFueS8zMTQ0MzA2Mzgz',
	'__insp_targlpt':'5Lit5Zu955_z5rK55Zu96ZmF5YuY5o6i5byA5Y_R5pyJ6ZmQ5YWs5Y_4X_W3peWVhuS%2FoeaBr1%2Fkv6HnlKjmiqXlkYpf6LSi5Yqh5oql6KGoX_eUteivneWcsOWdgOafpeivoi3lpKnnnLzmn6U%3D',
	'__insp_ss':'1549974683673',
	'__insp_norec_sess':'true',
	'cloud_token':'916d20134d214e108dd00d72d072f9f8',
	'_gat_gtag_UA_123487620_1':'1',
	'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1549976757',
	'__insp_slim':'1549976757086',
	'token':'227a46b7c0ac4badb74b2bfe443e359a',
	'_utm':'b21b42621eeb4d49b747000153d2a77f',
	'tyc-user-info':'%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25BB%25BA%25E5%25AE%2581%25E5%2585%25AC%25E4%25B8%25BB%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU0OTk3NjU1MywiZXhwIjoxNTY1NTI4NTUzfQ.SRWN6g82M3hnODFiKCwsthEKGaoQ0mnrRIsvtx2wo0brtxE3os8df3ZMHZRTMMnWCay87ZU4qSgAenpTAJmpFQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218979685279%2522%257D',
	'auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU0OTk3NjU1MywiZXhwIjoxNTY1NTI4NTUzfQ.SRWN6g82M3hnODFiKCwsthEKGaoQ0mnrRIsvtx2wo0brtxE3os8df3ZMHZRTMMnWCay87ZU4qSgAenpTAJmpFQ',
    }

	rs = requests.get(url, headers=headers, cookies=cookies, verify=False)

	# data_split = rs.text.split('(')[1].split(")")[0]
	data = BeautifulSoup(rs.text, "lxml")
	# print(data)
	return data

data_text = function();

# 公司logo
company_logo = data_text.find_all('div', class_="logo -w100")
for x in company_logo:
	company_logo_hash = x.find_all('img')[0].get('data-src')
	print('logo:'+company_logo_hash)

#公司名称 
header = data_text.find_all('h1', class_="name")[0].getText().strip()
print('名称:'+header)

# 公司电话
in_phone = data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[0].getText().strip()
# 公司邮箱
in_email = data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[1].getText().strip()
print('电话:'+in_phone)
print('邮箱:'+in_email)

# 公司网址
in_net = data_text.select('div.f0>div.in-block>a')[0].get("href")
# 公司地址
print('网址:'+in_net)
def address_():
	if "暂无信息" not in data_text.select('div.f0>div.in-block')[3].getText():
		in_address = data_text.select('div.f0>div.in-block')[3].getText().split('附近公司')[0]
		return in_address
	else:
		return "地址:暂无信息"
print(address_())

# 公司简介
summary = data_text.find_all('div', class_="summary")
for x in summary:
	company_summary_name = x.find_all('script')[0].getText().strip()
	print('简介:'+company_summary_name)



# 将信息写入csv
data_all = in_net + "," + address_()
write_file(data_all)
