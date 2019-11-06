# -*- coding: utf-8 -*-
import os,time
 
file_dir = "./test"
 
def file_name(file_dir):

	for root, dirs, files in os.walk(file_dir):
		jpg_list = []
		json_list = []

		for file in files:
			if os.path.splitext(file)[1] == '.jpg':
				jpg_list.append(os.path.splitext(file)[0])
			elif os.path.splitext(file)[1] == '.json':
				json_list.append(os.path.splitext(file)[0].split('.jpg')[0])
		# print(jpg_list)
		# print(json_list)

		i = 0
		for jpg_one in jpg_list:
			for json_one in json_list:
				if json_one == jpg_one:
					i = i + 1
					jpg_old_name = os.path.join(root,json_one+".jpg")
					jpg_new_name = os.path.join(root,json_one.split("_")[0]+"_"+str(i)+".jpg")
					json_old_name = os.path.join(root,json_one+".jpg.json")
					json_new_name = os.path.join(root,json_one.split("_")[0]+"_"+str(i)+".json")

					print(jpg_old_name)
					print(jpg_new_name)
					print(json_old_name)
					print(json_new_name)
					os.rename(jpg_old_name,jpg_new_name)
					os.rename(json_old_name,json_new_name)

				pass
			pass

file_name(file_dir)








# -*- coding: utf-8 -*-
import os,time,shutil

# 目录结构(以下都在同级目录,脚本也放在此级目录)
# lukou(所有路口放入此目录)
# mark
# mark1
# json
# 生成的ok目录位置与以上目录为同级目录


file_dir_one = "./lukou/"
mark1_path = "./mark1/"
json_path = "./json/"

ok_path = "./ok/"


def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

 
def file_name():

	one_list = {}
	for root_one, dirs_one, files_one in os.walk(file_dir_one):
		for d_file_one in files_one:
			one_list[d_file_one] = root_one

	for root_two, dirs_two, files_two in os.walk(mark1_path):
		for d_file_two in files_two:
			file_path = one_list[d_file_two].split('/')[-1]
			if '-' in file_path:
				img_name = file_path.split('-')[0]+"_"+file_path.split('-')[1]+".jpg"
			else:
				img_name = file_path+".jpg"
			# 老地址老名字
			old_img = root_two+"/"+d_file_two
			old_json = json_path+"/"+d_file_two+".txt"
			# 创建copy后的目录
			new_img_path = ok_path+file_path+"/"
			CheckDir(new_img_path)
			# 新地址新名字
			new_img = new_img_path+img_name
			new_json = new_img_path+img_name.split(".jpg")[0]+".txt"
			shutil.copy(old_img,new_img)
			shutil.copy(old_json,new_json)

file_name()             
             


