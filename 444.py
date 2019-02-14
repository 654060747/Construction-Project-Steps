# coding=utf-8
import requests
import os, sys,time, json, random, csv
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
# from tomorrow import threads
# import random
# 引入模块

#当前文件的路径
pwd = os.getcwd()
project_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
sys.path.append(project_path)

from api.rest_api import RestApi
# from daili import new_ip, del_ip

# 初始化
api = RestApi()

def create_tyc_company(data):
	try:
		api.tyc_company(data)
	except Exception as e:
		print (" api request fail 	. 	.		. ", format(e)) # 接口请求失败


def check_text_by_title(data_text, css):
	return data_text.select(css)[0].get('title')


def check_by_text(data_text, css):
	return data_text.select(css)[0].getText()

def check_one_company(url, data_text):
	code = url

	#  公司logo    logo             string
	company_logo = data_text.find_all('div', class_="logo -w100")
	for x in company_logo:
		logo = x.find_all('img')[0].get('data-src')
		print('logo:'+logo)

	# 公司名称     name             string
	name = data_text.find_all('h1', class_="name")[0].getText().strip()
	print('名称:'+name)

	# 电话        phone            string.
	# 
	# 
	if "暂无信息" not in data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[0].getText():
		phone = data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[0].getText().strip()
		print( "电话:"+phone)
	else:
		phone =""
		print( "电话:暂无信息" )

	# 邮箱        mail             string 
	if "暂无信息" not in data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[1].getText():
		mail = data_text.select('div.f0>div.in-block>span:nth-of-type(2)')[1].getText().strip()
		print( "邮箱:"+mail)
	else:
		mail =""

		print( "邮箱:暂无信息")
 
	# 网址        url              string
	if "暂无信息" in data_text.select('div.f0>div.in-block')[2].getText():
		print( "网址:暂无信息")

		url = ""
	else:
		url = data_text.select('div.f0>div.in-block>a')[0].get("href")
		print( "网址:"+url)

	# 地址        address          string
	if "暂无信息" not in data_text.select('div.f0>div.in-block')[3].getText():
		address = data_text.select('div.f0>div.in-block')[3].getText().split('附近公司')[0]
		print( address)
	else:
		print( "地址:暂无信息")
		address = ''

	# 简介        intro            string
	if "暂无信息" in data_text.find_all('div', class_="summary")[0].getText():
		print( "简介:暂无信息")
		intro = ''
	else:
		summary = data_text.find_all('div', class_="summary")
		for x in summary:
			intro = x.find_all('script')[0].getText().strip()
		print( "简介:"+intro )

	# 公司曾用名   old_name         string
	old_name_css = '#company_web_top > div.footer > div.refesh.float-left > span.updatetimeComBox'
	old_name = check_by_text(data_text, old_name_css)
	print('公司曾用名:'+old_name)

	# 更新时间     update_date      date
	update_date_css = '#company_web_top > div.footer > div.refesh.float-left > span.updatetimeComBox'
	update_date = check_by_text(data_text, update_date_css)
	print('更新时间:'+update_date)

	# 法人        boss_name        string
	boss_name_css = '#_container_baseInfo > table:nth-child(1) > tbody > tr:nth-child(1) > td.left-col.shadow > div > div:nth-child(1) > div.humancompany > div.name > a'
	boss_name = check_by_text(data_text, boss_name_css)
	print('法人:'+boss_name)

	# 注册资本     reg_money        string
	reg_money_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(1) > td:nth-child(2) > div'
	reg_money = check_text_by_title(data_text, reg_money_css)
	print('注册资本:'+reg_money)

	# 成立日期     set_date         string
	set_date_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(1) > td:nth-child(4) > div'
	set_date = check_text_by_title(data_text, set_date_css)
	print('成立日期:'+set_date)

	# 经营状态     status           string
	status_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(2) > td:nth-child(2)'
	status = check_by_text(data_text, status_css)
	print('经营状态:'+status)

	# 工商注册号    reg_number       string
	reg_number_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(2) > td:nth-child(4)'
	reg_number = check_by_text(data_text, reg_number_css)
	print('工商注册号:'+reg_number)

	# 统一社会信用代码 credit_code    string
	credit_code_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(3) > td:nth-child(2)'
	credit_code = check_by_text(data_text, credit_code_css)
	print('统一社会信用代码:'+credit_code)

	# 组织机构代码    company_code   string
	# company_code
	company_code_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(3) > td:nth-child(4)'
	company_code = check_by_text(data_text, company_code_css)
	print('组织机构代码:'+company_code)

	# 纳税人识别号   tax_code        string
	# tax_code
	tax_code_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(4) > td:nth-child(2)'
	tax_code = check_by_text(data_text, tax_code_css)
	print('纳税人识别号:'+tax_code)

	# 公司类型      category_id     integer
	# category_id
	category_id_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(4) > td:nth-child(4)'
	category_id = check_by_text(data_text, category_id_css)
	print('公司类型:'+category_id)

	# 营业期限      end_time        string
	# end_time
	end_time_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(5) > td:nth-child(2)'
	end_time = check_by_text(data_text, end_time_css)
	print('营业期限:'+end_time)

	# 行业         industry_id     integer
	# industry_id
	industry_id_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(5) > td:nth-child(4)'
	industry_id = check_by_text(data_text, industry_id_css)
	print('行业:'+industry_id)

	# 纳税人资质    tax              string
	# tax
	tax_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(6) > td:nth-child(2)'
	tax = check_by_text(data_text, tax_css)
	print('纳税人资质:'+tax)

	# 核准日期      allow_time       string
	# allow_time
	allow_time_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(6) > td:nth-child(4)'
	allow_time = check_by_text(data_text, allow_time_css)
	print('核准日期:'+allow_time)

	# 实缴资本      pay_money        string
	# pay_money
	pay_money_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(7) > td:nth-child(2)'
	pay_money = check_by_text(data_text, pay_money_css)
	print('实缴资本:'+pay_money)

	# 人员规模      all_people       string
	# all_people
	all_people_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(7) > td:nth-child(4)'
	all_people = check_by_text(data_text, all_people_css)
	print('人员规模:'+all_people)

	# 参保人数      insured_people   string
	# insured_people
	insured_people_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(8) > td:nth-child(2)'
	insured_people = check_by_text(data_text, insured_people_css)
	print('参保人数:'+insured_people)

	# 登记机关      organ            string
	# organ
	organ_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(8) > td:nth-child(4)'
	organ = check_by_text(data_text, organ_css)
	print('登记机关:'+organ)

	# 注册地址      reg_address      string
	# reg_address
	reg_address_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(9) > td:nth-child(2)'
	reg_address = check_by_text(data_text, reg_address_css)
	print('注册地址:'+reg_address)

	# 英文名称      en_name          string
	# en_name
	en_name_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(9) > td:nth-child(4)'
	en_name = check_by_text(data_text, en_name_css)
	print('英文名称:'+en_name)

	# 经营范围      operate_scope            string
	# operate_scope
	operate_scope_css = '#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(10) > td:nth-child(2) > span > span > span.js-full-container.hidden'
	operate_scope = check_by_text(data_text, operate_scope_css)
	print('经营范围:'+operate_scope)

	# 将信息写入csv
	# data_all = in_net + "," + address_()
	# write_file(data_all)

	# data_all = {'code': code, 'photo_num': photo_num, 'photo_hash': photo_hash, 'sign': 1, 'base_info': base_info, 'photos': photo_list }
	# create_user_with_photos(data_all)
	# code()
	data_all = {'code': code, 'city':city, 'logo': logo, 'name': name, 'phone': phone, 'mail': mail, 'url': url, 'address': address , 'intro': intro, 'url': url, 'url': url, 'url': url, 'url': url, 'url': url, 'url': url, 'url': url,
	'url': url, 'url': url, 'url': url, 'url': url, 'url': url, 'url': url, 'url': url, 'url': url}
	print(data_all)
	create_tyc_company(data_all)


def search_one_company(url, city):
	print("??????????????????????????????")
	CheckDir(file_name_load+"/"+ city)
	s=requests.session()
	headers={
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.9',
		'Connection':'keep-alive',
		'Host':'www.tianyancha.com',
		'Referer':url,
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
		'X-Requested-With':'XMLHttpRequest',
    }
	cookies={
		'TYCID':'c1218cf02e9f11e9911c9dc4171947d6',
		'undefined':'c1218cf02e9f11e9911c9dc4171947d6',
		'ssuid':'2545690930',
		'_ga':'GA1.2.839871124.1549931133',
		'_gid':'GA1.2.284325508.1549931133',
		'aliyungf_tc':'AQAAABYWFmNqmQsAFtfsdNM1IuM5YU9A',
		'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1549933125,1549992619,1550048239,1550126003',
		'__insp_wid':'677961980',
		'__insp_nv':'true',
		'__insp_targlpu':'aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v',
		'__insp_targlpt':'5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D',
		'__insp_ss':'1550126003276',
		'__insp_norec_sess':'true',
		'csrfToken':'ukFkD1V9imZa97igYNWx516o',
		'token':'6ef3a6b9c3db4da08f5b03bdb7ae090b',
		'_utm':'6dca78cd492047148589b17a1779205f',
		'tyc-user-info':'%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25BB%25BA%25E5%25AE%2581%25E5%2585%25AC%25E4%25B8%25BB%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDEyNjAyOSwiZXhwIjoxNTY1Njc4MDI5fQ.d9SO9pZv3VmLnDpTUJLkjMPnvgi4QTbzLpx9MyXo2KwfTDrHW-umxGDPfe_W8ORUtm64i1m5g6d1vATM4rjJDQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218979685279%2522%257D',
		'auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDEyNjAyOSwiZXhwIjoxNTY1Njc4MDI5fQ.d9SO9pZv3VmLnDpTUJLkjMPnvgi4QTbzLpx9MyXo2KwfTDrHW-umxGDPfe_W8ORUtm64i1m5g6d1vATM4rjJDQ',
		'RTYCID':'567f69e34b524548b208a31ac60da819',
		'CT_TYCID':'1c905500f40f4afaabd8504e96e4e91d',
		'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1550126381',
		'__insp_slim':'1550126381459',
		'cloud_token':'d910e1a89e494fb19bb69eb2c41b4802',
		'cloud_utm':'1807ed1f81264358a28a2f25665d6775',
    }

	rs = requests.get(url, headers=headers, cookies=cookies, verify=False)

	data = BeautifulSoup(rs.text, "lxml")
	# print(data)
	check_one_company(url, data)

 
##### 参数必须在上面定义
# @threads(20)

def write_file(data_list):

	file_name = file_name_load+"/北京/"+"68521782.csv"
	with open(file_name, 'a+', encoding='gbk') as f:
		writer = f.write(data_list+'\n')

file_name_load = "./download/user/"
def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

 












################# 




def write_file(data_list,city,page):

	file_name = file_name_load+city+".csv"
	with open(file_name, 'a+', encoding='gbk') as f:
		writer = f.write(data_list+","+page+'\n')

file_name_load = "./download/"
def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

# 主页面url
url="https://www.tianyancha.com"
# 用户登录
def open_page(url):
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

data_text = open_page(url);
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

	'TYCID':'c1218cf02e9f11e9911c9dc4171947d6',
	'undefined':'c1218cf02e9f11e9911c9dc4171947d6',
	'ssuid':'2545690930',
	'_ga':'GA1.2.839871124.1549931133',
	'_gid':'GA1.2.284325508.1549931133',
	'aliyungf_tc':'AQAAABYWFmNqmQsAFtfsdNM1IuM5YU9A',
	'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1549933125,1549992619,1550048239,1550126003',
	'__insp_wid':'677961980',
	'__insp_nv':'true',
	'__insp_targlpu':'aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v',
	'__insp_targlpt':'5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D',
	'__insp_ss':'1550126003276',
	'__insp_norec_sess':'true',
	'csrfToken':'ukFkD1V9imZa97igYNWx516o',
	'token':'6ef3a6b9c3db4da08f5b03bdb7ae090b',
	'_utm':'6dca78cd492047148589b17a1779205f',
	'tyc-user-info':'%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25BB%25BA%25E5%25AE%2581%25E5%2585%25AC%25E4%25B8%25BB%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDEyNjAyOSwiZXhwIjoxNTY1Njc4MDI5fQ.d9SO9pZv3VmLnDpTUJLkjMPnvgi4QTbzLpx9MyXo2KwfTDrHW-umxGDPfe_W8ORUtm64i1m5g6d1vATM4rjJDQ%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218979685279%2522%257D',
	'auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDEyNjAyOSwiZXhwIjoxNTY1Njc4MDI5fQ.d9SO9pZv3VmLnDpTUJLkjMPnvgi4QTbzLpx9MyXo2KwfTDrHW-umxGDPfe_W8ORUtm64i1m5g6d1vATM4rjJDQ',
	'_gat_gtag_UA_123487620_1':'1',
	'__insp_slim':'1550126066363',
	'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1550126066',

    }

	rs = requests.get(url, headers=headers, cookies=cookies, verify=False)

	# data_split = rs.text.split('(')[1].split(")")[0]
	data_list_city = BeautifulSoup(rs.text, "lxml")
	# print(data)
	return data_list_city

# 拿到各个公司的url
def company_city_url_new(company_data,city,page):
	list_city_url = company_data.select('div.content>div.header')
	for company_url in list_city_url:
		company_list_url = company_url.find_all('a')[0].get('href')
		print(company_list_url+"$"+city+"===="+page)
		write_file(company_list_url,city,page)

		search_one_company(company_list_url, city)


for p in range(1,6):
	url_p = 'https://www.tianyancha.com/search/p'+str(p)+'?base=bj'
	data_text_city = function_city(url_p)
	city = "北京"
	page = "p"+str(p)
	company_city_url_new(data_text_city,city,page)
# 字段名   |   参数   |  类型  |  说明
# -------------------------------------
# id          id              integer
# 序号        code             string
# 公司logo    logo             string
# 公司名称     name             string
# 公司曾用名   old_name         string
# 电话        phone            string
# 邮箱        mail             string
# 网址        url              string
# 地址        address          string
# 简介        intro            string
# 更新时间     update_date      date
# 法人        boss_name        string
# 
# 
# 注册资本     reg_money        string
# 成立日期     set_date         string
# 经营状态     status           string
# 工商注册号    reg_number       string
# 统一社会信用代码 credit_code    string
# 组织机构代码    company_code   string
# 纳税人识别号   tax_code        string
# 公司类型      category_id     integer
# 营业期限      end_time        string
# 行业         industry_id     integer
# 纳税人资质    tax              string
# 核准日期      allow_time       string
# 实缴资本      pay_money        string
# 人员规模      all_people       string
# 参保人数      insured_people   string
# 登记机关      organ            string
# 注册地址      reg_address      string
# 英文名称      en_name          string
# 经营范围      operate_scope            string
