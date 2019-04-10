import time
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup


def car_baoyang(char,driver):
	# 点击字母
	driver.find_element_by_css_selector("#div2 > li:nth-child("+str(char)+")").click()
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	# 得到每种字母下有多少品牌车
	car_list = data.select("#CarBrands > ul > li")
	lengh_car = len(car_list)

	for i in range(1,lengh_car):
		# 点击各品牌车
		driver.find_element_by_css_selector("#CarBrands > ul > li:nth-child("+str(i)+")").click()
		time.sleep(2)
		# 跳回点击各品牌车
		driver.find_element_by_css_selector("#div40 > div.CarHistoryTitlediv > div.CarHistoryTitleDel").click()




def by_tuhu_baoyang():
   

	driver = webdriver.Chrome()
	driver.get('https://by.tuhu.cn/baoyang/VE-ZAR-Giulia/pl2.0T-n2019.html')
	# 跳出选择车型界面
	driver.find_element_by_id("reSelectCar").click()
	time.sleep(3)


	for char in range(2,3):
		car_baoyang(char,driver)


by_tuhu_baoyang()


