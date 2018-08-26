# codeing:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import re
from pyquery import PyQuery as pq
import csv
from bs4 import BeautifulSoup

urls = ("http://zhao.resgain.net/name_list_", 
	  "http://qian.resgain.net/name_list_", 
	  "http://sun.resgain.net/name_list_", 
	  "http://li.resgain.net/name_list_", 
	  "http://zhou.resgain.net/name_list_", 
	  "http://wu.resgain.net/name_list_",
	  "http://zheng.resgain.net/name_list_", 
	  "http://wang.resgain.net/name_list_", 
	  "http://feng.resgain.net/name_list_", 
	  "http://chen.resgain.net/name_list_", 
	  "http://chu.resgain.net/name_list_", 
	  "http://wei.resgain.net/name_list_", 
	  "http://jiang.resgain.net/name_list_", 
	  "http://shen.resgain.net/name_list_", 
	  "http://han.resgain.net/name_list_",
	  "http://yang.resgain.net/name_list_", 
	  "http://zhu.resgain.net/name_list_", 
	  "http://qin.resgain.net/name_list_", 
	  "http://you.resgain.net/name_list_", 
	  "http://xu.resgain.net/name_list_", 
	  "http://ho.resgain.net/name_list_", 
	  "http://lu.resgain.net/name_list_", 
	  "http://shi.resgain.net/name_list_", 
	  "http://zhang.resgain.net/name_list_", 
	  "http://kong.resgain.net/name_list_", 
	  "http://tzao.resgain.net/name_list_", 
	  "http://yan.resgain.net/name_list_", 
	  "http://hua.resgain.net/name_list_", 
	  "http://jin.resgain.net/name_list_", 
	  "http://wei1.resgain.net/name_list_", 
	  "http://tao.resgain.net/name_list_", 
	  "http://jiang1.resgain.net/name_list_", 
	  "http://qi.resgain.net/name_list_", 
	  "http://xie.resgain.net/name_list_", 
	  "http://zou.resgain.net/name_list_", 
	  "http://yu.resgain.net/name_list_", 
	  "http://bai.resgain.net/name_list_", 
	  "http://shui.resgain.net/name_list_", 
	  "http://dou.resgain.net/name_list_", 
	  "http://zhang1.resgain.net/name_list_", 
	  "http://yun.resgain.net/name_list_", 
	  "http://su.resgain.net/name_list_", 
	  "http://pan.resgain.net/name_list_", 
	  "http://ge.resgain.net/name_list_", 
	  "http://xi.resgain.net/name_list_", 
	  "http://fan.resgain.net/name_list_", 
	  "http://peng.resgain.net/name_list_", 
	  "http://lang.resgain.net/name_list_", 
	  "http://lu1.resgain.net/name_list_", 
	  "http://wei2.resgain.net/name_list_", 
	  "http://chang.resgain.net/name_list_", 
	  "http://ma.resgain.net/name_list_", 
	  "http://miao.resgain.net/name_list_", 
	  "http://feng1.resgain.net/name_list_", 
	  "http://hua1.resgain.net/name_list_", 
	  "http://fang.resgain.net/name_list_", 
	  "http://yu1.resgain.net/name_list_", 
	  "http://ren.resgain.net/name_list_", 
	  "http://yuan.resgain.net/name_list_", 
	  "http://liu.resgain.net/name_list_", 
	  "http://feng2.resgain.net/name_list_", 
	  "http://bao.resgain.net/name_list_", 
	  "http://shi1.resgain.net/name_list_", 
	  "http://tang.resgain.net/name_list_", 
	  "http://fei.resgain.net/name_list_", 
	  "http://lian.resgain.net/name_list_", 
	  "http://cen.resgain.net/name_list_", 
	  "http://xue.resgain.net/name_list_", 
	  "http://lei.resgain.net/name_list_", 
	  "http://he.resgain.net/name_list_", 
	  "http://ni.resgain.net/name_list_", 
	  "http://tang1.resgain.net/name_list_", 
	  "http://teng.resgain.net/name_list_", 
	  "http://yin.resgain.net/name_list_", 
	  "http://lo.resgain.net/name_list_", 
	  "http://bi.resgain.net/name_list_", 
	  "http://hao.resgain.net/name_list_", 
	  "http://wu1.resgain.net/name_list_", 
	  "http://an.resgain.net/name_list_", 
	  "http://chang1.resgain.net/name_list_", 
	  "http://yue.resgain.net/name_list_", 
	  "http://yu2.resgain.net/name_list_", 
	  "http://shi2.resgain.net/name_list_", 
	  "http://fu.resgain.net/name_list_", 
	  "http://pi.resgain.net/name_list_", 
	  "http://bian.resgain.net/name_list_", 
	  "http://qi1.resgain.net/name_list_", 
	  "http://kang.resgain.net/name_list_", 
	  "http://wu2.resgain.net/name_list_", 
	  "http://yu3.resgain.net/name_list_", 
	  "http://yuan1.resgain.net/name_list_", 
	  "http://bu.resgain.net/name_list_", 
	  "http://gu.resgain.net/name_list_", 
	  "http://meng.resgain.net/name_list_", 
	  "http://ping.resgain.net/name_list_", 
	  "http://huang.resgain.net/name_list_", 
	  "http://he1.resgain.net/name_list_", 
	  "http://mu.resgain.net/name_list_", 
	  "http://xiao.resgain.net/name_list_", 
	  "http://yin1.resgain.net/name_list_", 
	  "http://yao.resgain.net/name_list_", 
	  "http://shao.resgain.net/name_list_", 
	  "http://zhan.resgain.net/name_list_", 
	  "http://wang1.resgain.net/name_list_", 
	  "http://qi2.resgain.net/name_list_", 
	  "http://mao.resgain.net/name_list_", 
	  "http://yu4.resgain.net/name_list_", 
	  "http://di.resgain.net/name_list_", 
	  "http://mi.resgain.net/name_list_", 
	  "http://bei.resgain.net/name_list_", 
	  "http://ming.resgain.net/name_list_", 
	  "http://zang.resgain.net/name_list_", 
	  "http://ji.resgain.net/name_list_", 
	  "http://fu1.resgain.net/name_list_", 
	  "http://cheng.resgain.net/name_list_",
	  "http://dai.resgain.net/name_list_", 
	  "http://tan.resgain.net/name_list_", 
	  "http://song.resgain.net/name_list_", 
	  "http://mao1.resgain.net/name_list_", 
	  "http://pang.resgain.net/name_list_", 
	  "http://xiong.resgain.net/name_list_", 
	  "http://ji1.resgain.net/name_list_", 
	  "http://shu.resgain.net/name_list_", 
	  "http://qu.resgain.net/name_list_", 
	  "http://xiang.resgain.net/name_list_", 
	  "http://zhu1.resgain.net/name_list_", 
	  "http://dong.resgain.net/name_list_", 
	  "http://liang.resgain.net/name_list_", 
	  "http://du.resgain.net/name_list_", 
	  "http://ruan.resgain.net/name_list_", 
	  "http://lan.resgain.net/name_list_", 
	  "http://min.resgain.net/name_list_", 
	  "http://xi1.resgain.net/name_list_", 
	  "http://ji2.resgain.net/name_list_", 
	  "http://ma1.resgain.net/name_list_", 
	  "http://qiang.resgain.net/name_list_", 
	  "http://jia.resgain.net/name_list_", 
	  "http://lu2.resgain.net/name_list_", 
	  "http://lou.resgain.net/name_list_", 
	  "http://wei3.resgain.net/name_list_", 
	  "http://jiang2.resgain.net/name_list_", 
	  "http://tong.resgain.net/name_list_", 
	  "http://yan1.resgain.net/name_list_", 
	  "http://guo.resgain.net/name_list_", 
	  "http://mei.resgain.net/name_list_", 
	  "http://sheng.resgain.net/name_list_", 
	  "http://lin.resgain.net/name_list_", 
	  "http://diao.resgain.net/name_list_", 
	  "http://tzeng.resgain.net/name_list_", 
	  "http://xu1.resgain.net/name_list_", 
	  "http://chiu.resgain.net/name_list_", 
	  "http://lo1.resgain.net/name_list_", 
	  "http://gao.resgain.net/name_list_", 
	  "http://xia.resgain.net/name_list_", 
	  "http://tzai.resgain.net/name_list_", 
	  "http://tian.resgain.net/name_list_", 
	  "http://fan1.resgain.net/name_list_", 
	  "http://hu.resgain.net/name_list_", 
	  "http://ling.resgain.net/name_list_", 
	  "http://huo.resgain.net/name_list_",
	  "http://yu5.resgain.net/name_list_", 
	  "http://wan.resgain.net/name_list_", 
	  "http://zhi.resgain.net/name_list_", 
	  "http://ke.resgain.net/name_list_", 
	  "http://zan.resgain.net/name_list_", 
	  "http://guan.resgain.net/name_list_", 
	  "http://lu3.resgain.net/name_list_", 
	  "http://mo.resgain.net/name_list_", 
	  "http://fang1.resgain.net/name_list_", 
	  "http://qiu.resgain.net/name_list_", 
	  "http://miao1.resgain.net/name_list_", 
	  "http://gan.resgain.net/name_list_", 
	  "http://xie1.resgain.net/name_list_", "http://ying.resgain.net/name_list_", "http://zong.resgain.net/name_list_", "http://ding.resgain.net/name_list_", "http://xuan.resgain.net/name_list_", "http://ben.resgain.net/name_list_", "http://deng.resgain.net/name_list_", "http://yi.resgain.net/name_list_", "http://shan.resgain.net/name_list_", "http://hang.resgain.net/name_list_", "http://hong.resgain.net/name_list_", "http://bao1.resgain.net/name_list_", "http://zhu2.resgain.net/name_list_", "http://zuo.resgain.net/name_list_", "http://shi3.resgain.net/name_list_", "http://tzui.resgain.net/name_list_", "http://ji3.resgain.net/name_list_", "http://niu.resgain.net/name_list_", "http://gong.resgain.net/name_list_", "http://cheng1.resgain.net/name_list_", "http://ji4.resgain.net/name_list_", "http://xing.resgain.net/name_list_", "http://hua2.resgain.net/name_list_", "http://pei.resgain.net/name_list_", "http://lu4.resgain.net/name_list_", "http://rong.resgain.net/name_list_", "http://ong.resgain.net/name_list_", "http://xun.resgain.net/name_list_", "http://yang1.resgain.net/name_list_", "http://fei1.resgain.net/name_list_", "http://zhen.resgain.net/name_list_", "http://qu1.resgain.net/name_list_", "http://jia1.resgain.net/name_list_", "http://feng3.resgain.net/name_list_", "http://zui.resgain.net/name_list_", "http://yi1.resgain.net/name_list_", "http://chu1.resgain.net/name_list_", "http://jin1.resgain.net/name_list_", "http://ji5.resgain.net/name_list_", "http://bing.resgain.net/name_list_", "http://mi1.resgain.net/name_list_", "http://song1.resgain.net/name_list_", "http://jing.resgain.net/name_list_", "http://duan.resgain.net/name_list_", "http://fu2.resgain.net/name_list_", "http://wu3.resgain.net/name_list_", "http://wu4.resgain.net/name_list_", "http://jiao.resgain.net/name_list_", "http://ba.resgain.net/name_list_", "http://gong1.resgain.net/name_list_", "http://mu1.resgain.net/name_list_", "http://kui.resgain.net/name_list_", "http://shan1.resgain.net/name_list_", "http://gu1.resgain.net/name_list_", "http://che.resgain.net/name_list_", "http://hou.resgain.net/name_list_", "http://mi2.resgain.net/name_list_", "http://peng1.resgain.net/name_list_", "http://quan.resgain.net/name_list_", "http://xi2.resgain.net/name_list_", "http://ban.resgain.net/name_list_", "http://yang2.resgain.net/name_list_", "http://qiu1.resgain.net/name_list_", "http://zhong.resgain.net/name_list_", "http://yi2.resgain.net/name_list_", "http://gong2.resgain.net/name_list_", "http://ning.resgain.net/name_list_", "http://qiu2.resgain.net/name_list_", "http://luan.resgain.net/name_list_", "http://bao2.resgain.net/name_list_", "http://gan1.resgain.net/name_list_", "http://tou.resgain.net/name_list_", "http://li1.resgain.net/name_list_", "http://rong1.resgain.net/name_list_", "http://zu.resgain.net/name_list_", "http://wu5.resgain.net/name_list_", "http://fu3.resgain.net/name_list_", "http://liu1.resgain.net/name_list_", "http://jing1.resgain.net/name_list_", "http://zhan1.resgain.net/name_list_", "http://shu1.resgain.net/name_list_", "http://long.resgain.net/name_list_", "http://ye.resgain.net/name_list_", "http://xing1.resgain.net/name_list_", "http://shu2.resgain.net/name_list_", "http://shao1.resgain.net/name_list_", "http://gao1.resgain.net/name_list_", "http://li2.resgain.net/name_list_", "http://ji6.resgain.net/name_list_", "http://pu.resgain.net/name_list_", "http://yin2.resgain.net/name_list_", "http://su1.resgain.net/name_list_", "http://bai1.resgain.net/name_list_", "http://why.resgain.net/name_list_", "http://pu1.resgain.net/name_list_", "http://tai.resgain.net/name_list_", "http://cong.resgain.net/name_list_", "http://oh.resgain.net/name_list_", "http://suo.resgain.net/name_list_", "http://xian.resgain.net/name_list_", "http://ji7.resgain.net/name_list_", "http://lai.resgain.net/name_list_", "http://zhuo.resgain.net/name_list_", "http://lin1.resgain.net/name_list_", "http://tu.resgain.net/name_list_", "http://mong.resgain.net/name_list_", "http://tzu.resgain.net/name_list_", "http://qiao.resgain.net/name_list_", "http://yang3.resgain.net/name_list_", "http://shi4.resgain.net/name_list_", "http://neng.resgain.net/name_list_", "http://tzang.resgain.net/name_list_", "http://shuang.resgain.net/name_list_", "http://wen.resgain.net/name_list_", "http://shen1.resgain.net/name_list_", "http://dang.resgain.net/name_list_", "http://zhai.resgain.net/name_list_", "http://tan1.resgain.net/name_list_", "http://gong3.resgain.net/name_list_", "http://lao.resgain.net/name_list_", "http://pang1.resgain.net/name_list_", "http://ji8.resgain.net/name_list_", "http://shen2.resgain.net/name_list_", "http://fu4.resgain.net/name_list_", "http://du1.resgain.net/name_list_", "http://ran.resgain.net/name_list_", "http://zai.resgain.net/name_list_", "http://li3.resgain.net/name_list_", "http://yong.resgain.net/name_list_", "http://chai.resgain.net/name_list_", "http://chi.resgain.net/name_list_", "http://sang.resgain.net/name_list_", "http://gui.resgain.net/name_list_", "http://pu2.resgain.net/name_list_", "http://niu1.resgain.net/name_list_", "http://shou.resgain.net/name_list_", "http://tong1.resgain.net/name_list_", "http://bian1.resgain.net/name_list_", "http://hu1.resgain.net/name_list_", "http://yan2.resgain.net/name_list_", "http://ji9.resgain.net/name_list_", "http://pu3.resgain.net/name_list_", "http://shang.resgain.net/name_list_", "http://nong.resgain.net/name_list_", "http://wen1.resgain.net/name_list_", "http://bei1.resgain.net/name_list_", "http://zhuang.resgain.net/name_list_", "http://yan3.resgain.net/name_list_", "http://tzai1.resgain.net/name_list_", "http://che1.resgain.net/name_list_", "http://yan4.resgain.net/name_list_", "http://chong.resgain.net/name_list_", "http://mu2.resgain.net/name_list_", "http://lian1.resgain.net/name_list_", "http://ru.resgain.net/name_list_", "http://xi3.resgain.net/name_list_", "http://huan.resgain.net/name_list_", "http://ai.resgain.net/name_list_", "http://yu6.resgain.net/name_list_", "http://rong2.resgain.net/name_list_", "http://xiang1.resgain.net/name_list_", "http://gu2.resgain.net/name_list_", "http://yi3.resgain.net/name_list_", "http://shen3.resgain.net/name_list_", "http://ge1.resgain.net/name_list_", "http://liao.resgain.net/name_list_", "http://yu7.resgain.net/name_list_", "http://zhong1.resgain.net/name_list_", "http://ji10.resgain.net/name_list_", "http://ju.resgain.net/name_list_", "http://heng.resgain.net/name_list_", "http://bu1.resgain.net/name_list_", "http://du2.resgain.net/name_list_", "http://geng.resgain.net/name_list_", "http://man.resgain.net/name_list_", "http://hong1.resgain.net/name_list_", "http://kuang.resgain.net/name_list_", "http://guo1.resgain.net/name_list_", "http://wen2.resgain.net/name_list_", "http://kou.resgain.net/name_list_", "http://kuang1.resgain.net/name_list_", "http://lu5.resgain.net/name_list_", "http://que.resgain.net/name_list_", "http://dong1.resgain.net/name_list_", "http://ou.resgain.net/name_list_", "http://shu3.resgain.net/name_list_", "http://wo.resgain.net/name_list_", "http://li4.resgain.net/name_list_", "http://yu8.resgain.net/name_list_", "http://yei.resgain.net/name_list_", "http://kui1.resgain.net/name_list_", "http://long1.resgain.net/name_list_", "http://shu4.resgain.net/name_list_", "http://gong4.resgain.net/name_list_", "http://she.resgain.net/name_list_", "http://nie.resgain.net/name_list_", "http://chao.resgain.net/name_list_", "http://gou.resgain.net/name_list_", "http://ao.resgain.net/name_list_", "http://rong3.resgain.net/name_list_", "http://leng.resgain.net/name_list_", "http://zi.resgain.net/name_list_", "http://xin.resgain.net/name_list_", "http://kan.resgain.net/name_list_", "http://na.resgain.net/name_list_", "http://jian.resgain.net/name_list_", "http://rao.resgain.net/name_list_", "http://kong1.resgain.net/name_list_", "http://tzeng1.resgain.net/name_list_", "http://wu6.resgain.net/name_list_", "http://sha.resgain.net/name_list_", "http://nie1.resgain.net/name_list_", "http://yang4.resgain.net/name_list_", "http://ju1.resgain.net/name_list_", "http://shi5.resgain.net/name_list_", "http://feng4.resgain.net/name_list_", "http://tzao1.resgain.net/name_list_", "http://guan1.resgain.net/name_list_", "http://kuai.resgain.net/name_list_", "http://xiang2.resgain.net/name_list_", "http://chah.resgain.net/name_list_", "http://hou1.resgain.net/name_list_", "http://jing2.resgain.net/name_list_", "http://hong2.resgain.net/name_list_", "http://you1.resgain.net/name_list_", "http://zhu3.resgain.net/name_list_", "http://quan1.resgain.net/name_list_", "http://dai1.resgain.net/name_list_", "http://yi4.resgain.net/name_list_", "http://huan1.resgain.net/name_list_", "http://gong5.resgain.net/name_list_", "http://moqi.resgain.net/name_list_", "http://shuma.resgain.net/name_list_", "http://shangguan.resgain.net/name_list_", "http://ooyang.resgain.net/name_list_", "http://shaho.resgain.net/name_list_", "http://zuguo.resgain.net/name_list_", "http://wenren.resgain.net/name_list_", "http://dongfang.resgain.net/name_list_", "http://helian.resgain.net/name_list_", "http://huangfu.resgain.net/name_list_", "http://yuchi.resgain.net/name_list_", "http://gongyang.resgain.net/name_list_", "http://tantai.resgain.net/name_list_", "http://gongye.resgain.net/name_list_", "http://zongzheng.resgain.net/name_list_", "http://puyang.resgain.net/name_list_", "http://chunyu.resgain.net/name_list_", "http://shanyu.resgain.net/name_list_", "http://taishu.resgain.net/name_list_", "http://shentu.resgain.net/name_list_", "http://gongsun.resgain.net/name_list_", "http://zhongsun.resgain.net/name_list_", "http://xuanyuan.resgain.net/name_list_", "http://linghu.resgain.net/name_list_", "http://xuli.resgain.net/name_list_", "http://yuwen.resgain.net/name_list_", "http://zhangsun.resgain.net/name_list_", "http://murong.resgain.net/name_list_", "http://situ.resgain.net/name_list_", "http://sikong.resgain.net/name_list_", "http://lou1.resgain.net/name_list_", "http://chu2.resgain.net/name_list_")

browser = webdriver.Chrome()  # 打开浏览器，浏览器打开一次即可

# 数据写入csv文件
def write_file(name,count):

	with open('name.csv', 'a+', encoding='utf-8') as f:

		writer = f.write(name+",")
		# 10个换行
		if (count%10 == 0):
			writer = f.write("\n")
		#先写入columns_name
	pass

# 数据处理
def data_name(url,i):

	#拼接完整的url
	url_full = url + str(i) + '.html'

	browser.get(url_full)  # 进入相关网站

	html = browser.page_source  # 获取网站源码

	data = str(pq(html))  # str() 函数将对象转化为适于人阅读的形式。

	# print(data)
	data = BeautifulSoup(data)

	# 先找到class属性对应的div
	name_all = data.find_all('div',{'class':'col-xs-12'})

	for div in name_all:

		# 在div下找到class属性对应的a标签
		ass = div.find_all('a',{'class':'btn btn-link'})

		# print(len(ass))
		# a标签存在继续，a标签为null跳过
		if len(ass)>0:
			# print(ass[0].getText())

			# 计数
			count = 0
			for name_list in ass:

				count = count + 1
				# 取值
				name = name_list.getText()
				# 不换行打印
				# print(name,end=",")

				write_file(name,count) #方法调用

				# 10个换行一次
				# if (count%10 == 0):
				# 	print("")
	pass

# 循环url并实现1到10页的自动跳转
for url in urls:

	# print(url)

	for i in range(1,11):
				
		# print(i)
		# 方法调用
		data_name(url,i)

