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

def write_file(data_list,city,page):

	file_name = file_name_load+city+".csv"
	with open(file_name, 'a+', encoding='gbk') as f:
		writer = f.write(data_list+","+page+'\n')

file_name_load = "./download/url/"
def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

# 主页面url
url="https://www.tianyancha.com"
# 用户登录
def function(url):


	CheckDir(file_name_load)

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

data_text = function(url);
# print(data_text)

# 初始化集合
list_data = []
# 拿到各个城市url
def city_url(data_):
	# city_url_l = data_.find_all('div', class_="item -single")
	# for x in city_url_l:
	# 	company_city_url = x.find_all('a')[0].get('href')
	# 	company_city_blank = x.getText()
	# 	# print(company_city_url)
	# 	list_data.append(company_city_url+"$"+company_city_blank)

	city_urls_new = data_.find_all('a', class_="link-hover-click overflow-width")
	for x in city_urls_new:
		company_city_urls_new = x.get('href')
		company_city_urls_blank = x.getText()
		list_data.append(company_city_urls_new+"$"+company_city_urls_blank)

	# city_urls = data_.select('div.row>div.col-11>div.item>a')
	# for x in city_urls:
	# 	company_city_urls = x.get('href')
	# 	company_city_urls_blank = x.getText()
	# 	list_data.append(company_city_urls+"$"+company_city_urls_blank)
	# return list_data

# city_url(data_text)
# print(list_data)

# list_p_city_url = []
# for x in list_data:
# 	for p in range(1,251):
# 		p_city = (x.split('?')[0]+"/p"+str(p)+"?"+x.split('?')[1]).split("$")[0]
# 		city = x.split("$")[1]
# 		page = "p"+str(p)
# 		# print(p_city)
# 		# list_p_city_url.append(p_city)
# 		write_file(p_city, city, page)


# 进入每个城市
def function_city(url):

	CheckDir(file_name_load)
	# url = [0]
	s=requests.session()
	headers={

	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'Host':'www.tianyancha.com',
	'Referer':url,
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest',

    }

	cookies={

	'TYCID':'e41e6c502eb811e982cbc392d8a84c8f',
	'undefined':'e41e6c502eb811e982cbc392d8a84c8f',
	'ssuid':'3855799584',
	'_ga':'GA1.2.678265784.1549970952',
	'_gid':'GA1.2.1653442593.1549970952',
	'RTYCID':'d4ca626473f8440e82e251a87c8913a0',
	'CT_TYCID':'fa16f903a9854218b2faca9fc7d1da8c',
	'__insp_wid':'677961980',
	'__insp_nv':'true',
	'__insp_targlpu':'aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v',
	'__insp_targlpt':'5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D',
	'__insp_ss':'1550061292020',
	'__insp_norec_sess':'true',
	'aliyungf_tc':'AQAAAI64yCiTLAcALrbrdJuCLrPjNEml',
	'csrfToken':'t0MH8c9mEhy-8fLNRGgTY3Qv',
	'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1549977249,1550061291,1550062521,1550064895',
	'token':'7d766bf9f0b242cc9c1d413577b659fc',
	'_utm':'87eeddd0811d46cabca300833586e3ba',
	'tyc-user-info':'%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25BB%25BA%25E5%25AE%2581%25E5%2585%25AC%25E4%25B8%25BB%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDA2NDY4NywiZXhwIjoxNTY1NjE2Njg3fQ.ALDp3WAYYGZEw8UjQMXbZYCGIpDRzzChzpKcne0nIL6PMfyZVSgt2fhpWFJHy7v__Kn4p7jQxLZ2thfLmJDLIA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218979685279%2522%257D',
	'auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDA2NDY4NywiZXhwIjoxNTY1NjE2Njg3fQ.ALDp3WAYYGZEw8UjQMXbZYCGIpDRzzChzpKcne0nIL6PMfyZVSgt2fhpWFJHy7v__Kn4p7jQxLZ2thfLmJDLIA',
	'cloud_token':'29d6cd338fbe4bf69ccb8d5cbea21407',
	'cloud_utm':'b6581437fc104b88b5054fdda219257a',
	'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1550065160',
	'_gat_gtag_UA_123487620_1':'1',
	'__insp_slim':'1550065160005',

    }

	rs = requests.get(url, headers=headers, cookies=cookies, verify=False)

	# data_split = rs.text.split('(')[1].split(")")[0]
	data_list_city = BeautifulSoup(rs.text, "lxml")
	# print(data)
	return data_list_city

# 拿到各个公司的url
def company_city_url_new(company_data,city,page):
	list_city_url = company_data.select('div.content>div.header>a')
	for company_url in list_city_url:
		company_list_url = company_url.get('href')
		print(company_list_url+"$"+city+"===="+page)
		write_file(company_list_url,city,page)

for p in range(1,6):
	url_p = 'https://www.tianyancha.com/search/p'+str(p)+'?base=ah'
	data_text_city = function_city(url_p)
	city = "安徽"
	page = "p"+str(p)
	company_city_url_new(data_text_city,city,page)
	# print(company_city_url_new(data_text_city,city))



# 测试一条数据
# data_text_city = function_city(list_p_city_url[0].split("$")[0])
# print(company_city_url_new(data_text_city))
# print(list_p_city_url[2].split("$")[0])

# company_data_text = function(company_list_data[0])
# print(company_list_data[0])
# # 公司logo
# company_logo = company_data_text.find_all('div', class_="logo -w100")
# for x in company_logo:
# 	company_logo_hash = x.find_all('img')[0].get('data-src')
# 	print('logo:'+company_logo_hash)

# #公司名称 
# header = company_data_text.find_all('h1', class_="name")[0].getText().strip()
# print('名称:'+header)

# # 公司电话
# in_phone = company_data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[0].getText().strip()
# # 公司邮箱
# in_email = company_data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[1].getText().strip()
# print('电话:'+in_phone)
# print('邮箱:'+in_email)

# # 公司网址
# in_net = company_data_text.select('div.f0>div.in-block>a')[0].get("href")
# # 公司地址
# print('网址:'+in_net)
# def address_():
# 	if "暂无信息" not in company_data_text.select('div.f0>div.in-block')[3].getText():
# 		in_address = company_data_text.select('div.f0>div.in-block')[3].getText().split('附近公司')[0]
# 		return in_address
# 	else:
# 		return "地址:暂无信息"
# print(address_())

# # 公司简介
# summary = company_data_text.find_all('div', class_="summary")
# for x in summary:
# 	company_summary_name = x.find_all('script')[0].getText().strip()
# 	print('简介:'+company_summary_name)



