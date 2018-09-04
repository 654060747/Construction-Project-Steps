# coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from tomorrow import threads

# 引入模块
# from RestApi import RestApi

# 初始化
# api = RestApi()

#  创建处理记录
#  api.create_record(name)
#    传入参数:
#         name:  2018-04-09 晴 上午
#     返回参数 : 14


s_id = 4800000  # 11310961

# e_id = 1491211
e_id = 7800000


# def create_user(data):
#     try:
#         api.create_user(data)
#     except Exception as e:
#         print (" api request fail   .   .       . ", format(e)) # 接口请求失败


def write_file(data):
    file_name=str(s_id)+"_"+str(e_id)+".csv"
    # print(file_name)
    with open(file_name, 'a+') as f:
        writer = f.write(data+'\n')

@threads(100)
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
                    print (num)
                    photo_hash = photo_lik.split('uid_hash=')[1].split('&')[0]
                    # http://photo.jiayuan.com/showphoto.php?uid_hash=97513ed75d4ee0b49977540cc28adeea&tid=0&cache_key=
                    #调用接口
                    # d = {'uid': sn, 'photo_num': num, 'photo_hash': photo_hash, 'sign': 1, }
                    # create_user(d)

                    # #写文件
                    write_file(data)
        except Exception as e:
            print (".       .   .   .       . ", format(e)) # 没有照片
    except Exception as e:
        print("x        .       .   .   x", format(e))  # 账户已关闭


##### 参数必须在上面定义
@threads(200)
def visit_page(sn):
    url="http://www.jiayuan.com/" + str(sn)
    s=requests.session()
    headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '***',
    'Referer': 'http://www.jiayuan.com/157709283'
    }
    cookies={'COMMON_HASH': '458225a40acaf6bd4285d1c23da31052', 'PROFILE': '182103006%3Awahaha%3Am%3Aimages1.jyimg.com%2Fw4%2Fglobal%2Fi%3A0%3A%3A1%3Azwzp_m.jpg%3A1%3A1%3A50%3A10', 'RAW_HASH': 'L8Jg4BcmaAct40qhEmmlPZIE55FwGT6YPbuTi60Qnk52xDPDdKg9z7KIx7Jw9rInn50IbHcJcoBdYyIdRh9a2E8pi0r56Vyb3RcD3Tks5RwcVqE.', 'SESSION_HASH': 'f6f012d2bd2f4050d3a3d913db6bb4e602aec7f6', 'last_login_time': '1535985118', 'myage': '26', 'myincome': '30', 'myloc': '31%7C3101', 'mysex': 'm', 'myuid': '181103006', 'pop_avatar': '1', 'save_jy_login_name': '17521507650', 'sl_jumper': '%26cou%3D17%26omsg%3D0%26dia%3D0%26lst%3D2018-09-03', 'stadate1': '181103006', 'upt': 'dXqWdUrSFGm77AGzvxxoHQr9d8tqcuPXAcmZaIvd0wBwdvUQ1DhPu3cEKBjT1MINrf-lbMAbMRvNDz4oZz3RVaMf', 'user_attr': '000000', 'PHPSESSID': '104914b51ef6f9cd1b03ba4bc9422587', 'main_search:182103006': '%7C%7C%7C00', 'registeruid': '182103006'}

    rs = requests.get(url, headers=headers, cookies=cookies, verify=False)
    rs.encoding='utf-8'
    # print(rs.text)
    data = BeautifulSoup(rs.text, "lxml")
    check_html(data, sn)

for i in range(s_id,e_id):
    # print(url)
    visit_page(i)
