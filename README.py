# coding=utf-8
import requests
import time, json
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
# from tomorrow import threads
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

	file_name = str(s_id)+"_"+str(e_id)+".csv"
	with open(file_name, 'a+', encoding='utf-8') as f:
		writer = f.write(data_list+'\n')

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

def function(i):
	
	url="http://search.baihe.com/search/getUserList?userIDs=" + str(i)
	# s=requests.session()
	headers={
	'Host': 'search.baihe.com',
	'Connection': 'keep-alive',
	'Content-Length': '0',
	'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
	'Origin': 'http://search.baihe.com',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
	'Referer': 'http://search.baihe.com/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9'
	}
	cookies={'accessID':'20180830213130345386', 'channel':'baidu-pp', 'code':'350002-001', 'tempID':'8334593585', 'NTKF_T2D_CLIENTID':'guest4E594A3D-73FE-15B1-6CC9-8B082361EBAC', 'OnceLoginWEB':'160000111', 'noticeEvent_160000111':'6', 'lastLoginDate':'Thu%20Sep%2006%202018%2020%3A56%3A34%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29', 'orderSource':'10130301', 'accessToken':'BH1536238596331834860', 'AuthCookie':'4BFFD62B611D896E3A6113EF4F137DD8F9DEC8A2183459196CA47152EB9AB22C7A31BFECC93FE002904AF051C2A81FF4D7A6E2425F8EA858724C0FB1BF12EE51BAFBA6824F78EDC26BFB0F813A653583', 'AuthMsgCookie':'783D3AF2400859BDB117E27B83F5C483AC4B272BE51CB460770B00C53EB9DEFF997116A437CD3071AA6EBCB4307D3F0ADD23DFE55B3B46E20D3A574E8977C355DA71571AE464B2BC1107B5F06A4EE8C4', 'GCUserID':'160000111', 'LoginEmail':'18979685279%40mobile.baihe.com', 'userID':'160000111', 'spmUserID':'160000111', 'nTalk_CACHE_DATA':'{uid:kf_9847_ISME9754_160000111,tid:1536238596447991}', 'hasphoto':'1', 'AuthCheckStatusCookie':'53545970483051C487A95FB90C2AEBA514D1D3015978705726A127B203C4931405E9D878DCC812E7', 'cookie_pcc':'%7C%7Cbaidu-pp%7C%7C350002-001%7C%7Chttps%3A//www.baidu.com/s%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3Dbaihewang%26rsv_pq%3Df826a7330004a897%26rsv_t%3D46ffTPvfOkL6Q3Xc%252Fppaq1F7WCyyTs8JFXmqIbfQYQ9fHHUSozBeOQUNV2k%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D9%26rsv_sug1%3D8%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D1575%26rsv_sug4%3D1575%26rsv_sug%3D1', 'Hm_lvt_5caa30e0c191a1c525d4a6487bf45a9d':'1536234728,1536238337,1536238596,1536239479', 'Hm_lpvt_5caa30e0c191a1c525d4a6487bf45a9d':'1536239485', '_fmdata':'PLlocuoMKsUBrQjVkVCDj6teG9YUWgw9ZvCP6M4M6POpK8WO1rmmBhAmn%2FxmPNwF%2B9BxmW3hYvYHs1DhxsfiwOLMMXpHwBbFWvN3brmaENU%3D'}

	rs = requests.get(url, headers=headers, cookies=cookies, verify=False)

	# data_split = rs.text.split('(')[1].split(")")[0]
	# print(data)

	data_json = json.loads(rs.text)
	# print(data_list)

	#原数据性别是以0或者1或者null表示的
	gender = str(data_json['data'][0]['gender'])

	if gender == '0':
		gender = '女'
	elif gender == '1':
		gender = '男'
	else:
		gender = '不男不女'

	photo_list = ''
	int_i = len(data_json['data'][0]['photoList'])
	if int_i >= 3:
		for i in range(0, int_i):
			photo = data_json['data'][0]['photoList'][i]+","
			photo_list += photo
		
		# data_list = str(int_i) + "," + str(data_json['data'][0]['userID']) + "," + gender + "," + str(data_json['data'][0]['age']) + "," + str(data_json['data'][0]['height']) + "," + photo_list 
		# print(data_list)
		# write_file(data_list)

		# photos = ['1', "2", "2"]

		d = {'uid': str(data_json['data'][0]['userID']), 'photo_num': str(int_i), 'photo_hash': ' ', 'sign': 2, 'photos': photo_list }

		create_user_with_photos(d)

	pass

# function(s_id)


for i in range(s_id,e_id):
	
    function(i)
#     # time.sleep(10) 
