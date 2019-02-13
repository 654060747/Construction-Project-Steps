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

	file_name = file_name_load+"/城市/"+"城市id.csv"
	with open(file_name, 'a+', encoding='gbk') as f:
		writer = f.write(data_list+'\n')

file_name_load = "./download"
def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

def function():

	url="https://www.tianyancha.com/company/68521782"

	CheckDir(file_name_load+"/城市/")

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
	
	'TYCID':'4a83d2a02f9011e99862f9cee76ba5b8',
	'undefined':'4a83d2a02f9011e99862f9cee76ba5b8',
	'ssuid':'9315529300',
	'_ga':'GA1.2.720773162.1550063471',
	'_gid':'GA1.2.1747029550.1550063471',
	'__insp_wid':'677961980',
	'__insp_nv':'true',
	'__insp_targlpu':'aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v',
	'__insp_targlpt':'5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D',
	'__insp_ss':'1550063472067',
	'__insp_norec_sess':'true',
	'RTYCID':'08877c6927fa4fdeab5573e717a90189',
	'CT_TYCID':'2eb283b662024639981092a3c75070c1',
	'aliyungf_tc':'AQAAAESv3F09AwwALrbrdLlWS6mFZnQ7',
	'csrfToken':'V_rwWiHsMaFwDQCRz3y4QG_k',
	'Hm_lvt_e92c8d65d92d534b0fc290df538b4758':'1550063471,1550063709,1550063831,1550066413',
	'token':'4404bc475b4a4edc8c5ff872d980663b',
	'_utm':'4797958d8964449c95d6dba4ce2d8012',
	'tyc-user-info':'%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25BB%25BA%25E5%25AE%2581%25E5%2585%25AC%25E4%25B8%25BB%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDA2NjE5NywiZXhwIjoxNTY1NjE4MTk3fQ.qnQ_CtRy3Ocpzg6eLCHsJBr6C4mUs6Z1Czrq5C00jxWw28RkeUfsRbBie4PPtNDWtdFAywKmpZO1WkW8iQFRgA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218979685279%2522%257D',
	'auth_token':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODk3OTY4NTI3OSIsImlhdCI6MTU1MDA2NjE5NywiZXhwIjoxNTY1NjE4MTk3fQ.qnQ_CtRy3Ocpzg6eLCHsJBr6C4mUs6Z1Czrq5C00jxWw28RkeUfsRbBie4PPtNDWtdFAywKmpZO1WkW8iQFRgA',
	'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758':'1550066492',
	'__insp_slim':'1550066492615',
	'cloud_token':'6a7cf80541e242ce9583d1c680303af1',
	'cloud_utm':'3599d0f37eb24699b0029b98bec1ceae',

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
