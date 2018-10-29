import csv
import time
import os

# 同级目录新建一个text.txt文本，内容以逗号隔开
file_txt = open('test.txt')
csv_name = file_txt.read().split(',')[0].strip()
file_txt = open('test.txt')
file_list = file_txt.read().split(',')[1].strip()
# 读取csv文件
csv_file = csv.reader(open(csv_name,'r'))
# # 遍历文件内容
for x in csv_file:
	print(x)
	# time.sleep(0.1)
	# 打开file_list文件夹
	movie_name = os.listdir('./'+file_list)
	# 遍历gege文件
	for temp in movie_name:
		# csv文件取得的内容是否与file_list文件夹下的文件名相同
		if x[0] == os.path.basename(temp):
			# 再打开下一级目录
			update_name = os.listdir('./'+file_list+'/'+temp)
			# 遍历二级文件
			for one_file in update_name:
				new_name = os.path.basename(temp)
				if '.' in one_file:
					os.rename('./'+file_list+'/'+temp+'/'+one_file,'./'+file_list+'/'+temp+'/'+new_name+'.'+one_file.split('.')[1])
				else:
					os.rename('./'+file_list+'/'+temp+'/'+one_file,'./'+file_list+'/'+temp+'/'+new_name)

					
					
					
					
										
					
# coding = utf-8
import os


# 文件目录
root_path = "./gege/" # csv.reader(open(csv_name,'r'))
# 年与月之间需要修改的原名字
original_name = "零拾"
# 年与月之间修改后的名字
make_name = "壹拾"



file_name = os.listdir(root_path)
# 遍历文件内容
for name in file_name:
	# print(x)
	try:
		sect_name = name.split("年")[1].split("月")[0]
		print(sect_name)

		if original_name in sect_name:

			new_name = name.split("年")[0]+"年"+make_name+"月"+name.split("月")[1]
			print(new_name)
			os.rename(root_path+name, root_path+new_name)

	except Exception as e:
		print("====缺少年月===="+name)
	
