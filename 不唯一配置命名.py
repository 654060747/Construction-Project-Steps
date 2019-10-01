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
				json_list.append(os.path.splitext(file)[0])
		# print(jpg_list)
		# print(json_list)

		i = 0
		for jpg_one in jpg_list:
			for json_one in json_list:
				if json_one == jpg_one:
					i = i + 1
					jpg_old_name = os.path.join(root,json_one+".jpg")
					jpg_new_name = os.path.join(root,json_one.split("_")[0]+"_"+str(i)+".jpg")
					json_old_name = os.path.join(root,json_one+".json")
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


