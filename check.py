#! -coding:utf8 -*-
import requests
import time
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from tomorrow import threads
import random
# 引入模块
from RestApi import RestApi
from daili import new_ip, del_ip

# 初始化
api = RestApi()

#  创建处理记录
#  api.create_record(name)
#    传入参数:
#         name:  2018-04-09 晴 上午
#     返回参数 : 14
s_id = 10238074  # 11310961
# e_id = 1491211
e_id = 13000000

def create_user(data):
	try:
		api.create_user(data)
	except Exception as e:
		print (" api request fail 	. 	.		. ", format(e)) # 接口请求失败

##### 参数必须在上面定义
# @threads(20)

def write_file(data):
	file_name=str(s_id)+"_"+str(e_id)+".csv"
	# print(file_name)
	with open(file_name, 'a+') as f:
		writer = f.write(data+'\n')

@threads(5)
def check_html(data, sn):
	try:
		nav_text = data.find_all('ul', class_="nav_l")[0]
		photo_text = nav_text.find_all('li')[1]
		photo_title = photo_text.text
		photo_lik=photo_text.find('a').get("href")

		# print(photo_title)
		# print(photo_lik)
		try:
			if "的照片" in photo_title:
				num = int(photo_title.split('(')[1].strip(")"))
				if num > 2 :
					data = str(num) + "," + str(sn)  + "," + photo_lik
					# print (num)
					photo_hash = photo_lik.split('uid_hash=')[1].split('&')[0]
					# http://photo.jiayuan.com/showphoto.php?uid_hash=97513ed75d4ee0b49977540cc28adeea&tid=0&cache_key=
					#调用接口
					# print( sn + "========================================")
					d = {'uid': sn, 'photo_num': num, 'photo_hash': photo_hash, 'sign': 1, }
					create_user(d)

					# #写文件
					# write_file(data)
		except Exception as e:
			print ("no photo.		. 	. 	.		. ", format(e)) # 没有照片
	except Exception as e:
		print(" x		.		. 	. 	x", format(e))  # 账户已关闭

# @threads(5)
def visit_page(sn, proxies):
	url="http://www.jiayuan.com/" + str(sn)
	s=requests.session()
	headers={
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Host': '***',
	'Referer': url
	}
	cookies = {'PROFILE': '182103006%3Awahaha%3Am%3Aat1.jyimg.com%2F45%2F52%2F8225a40acaf6bd4285d1c23da310%3A1%3A%3A1%3A8225a40ac_1_avatar_p.jpg%3A1%3A1%3A50%3A10', 'myloc': '31%7C3101', 'myage': '26', 'myincome': '30', 'last_login_time': '1536150497', 'mysex': 'm', 'PHPSESSID': 'b884a3f9484f0acc9680d9e0bb8a7ebd', 'myuid': '181103006', 'stadate1': '181103006', 'sl_jumper': '%26cou%3D17%26omsg%3D0%26dia%3D0%26lst%3D2018-09-05','RAW_HASH': 'W0%2Ax7J9AeQpzsY1MAVKQUmUEWAlAa5McwOhKj6V8t216g2rIXJrip7kY3IuWVoDrc2MhCEpNQDs11CTmb7FKeQZI2rJSeNPzAA-4Qe7e3V1PLxg.', 'user_attr': '000000', 'registeruid': '182103006', 'COMMON_HASH': '458225a40acaf6bd4285d1c23da31052', 'upt': 'qYnK%2Ai56DEDZysXOVhRBChPueb-IdGZ-NPrqFzoCzKqmgVbJM0N-BapbmMW-eoaZQVG3jNffaq5ZI%2AiNiegs9I5K', 'SESSION_HASH': '02c19e1fc961534fba7074267d4595d21e77a91e', 'save_jy_login_name': '17521507650', 'main_search:182103006': '%7C%7C%7C00'}
	try:
		rs = requests.get(url, proxies=proxies,  headers=headers,	cookies=cookies, verify=False)
		rs.encoding = 'utf-8'
		# print(rs.text)
		data = BeautifulSoup(rs.text, "lxml")
		check_html(data, sn)
	except Exception as e:
		proxies = new_ip()


proxies = new_ip()

for i in range(s_id,e_id):
	print(i)
	visit_page(i, proxies[0])

	if i % 10000 == 0:
		# del_ip(proxies[1])
		proxies = new_ip()
	# time.sleep(random.random())
	# print(i % 100000 == 0)
	# if i % 100000 == 0:
	# 	visit_page(i, proxies[0])
	# 	print("应该删除了=======")
	# 	# del_ip(proxies[1])
	# 	proxies = new_ip()
	# else:
	# 	visit_page(i, proxies[0])

	# if not proxies:
	# 	print('代理 ip 已经耗尽.. %s' % (i))
	# 	break

	# print(i % 5000)
	# visit_page(i, proxies[0])

	# if proxies:
	# 	print(i)
	# else:
	# 	print('代理 ip 已经耗尽.. %s' % (i))
	# 	break

	# if i % 10000 == 0:
	# 	del_ip(proxies[1])
	# 	proxies = new_ip()
