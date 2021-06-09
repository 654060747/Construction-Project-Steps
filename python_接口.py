from flask import Flask,request
import json,csv

# 把当前的python文件当做一个服务
app=Flask(__name__)

def is_net(return_dict):
    return_dict['return_code'] = '5004'
    return_dict['return_info'] = '请求参数为空'
    return json.dumps(return_dict, ensure_ascii=False)


# 只接受get方法访问
@app.route("/test",methods=["GET"])
def check():
    # 默认返回内容
    return_dict= {'return_code': '200','return_info': '请求成功','result': False}
    # 获取传入的参数
    # 设置get方法参数
    # ID = request.args.to_dict().get('id')
    # age = request.args.to_dict().get('age')
    # if not ID or not age:
    #     return is_net(return_dict)
    # 对参数进行操作
    # return_dict['name']=name
    return_dict['result']=get_data()

    return json.dumps(return_dict, ensure_ascii=False)
 
# 功能函数
def get_data():
    csv_file = csv.reader(open('data.csv','r'))
    data_ = []
    for line in csv_file:
        ID = line[0]
        url = line[1]
        result_str={'id':ID,'url':url}
        data_.append(result_str)
    return data_
 
if __name__ == "__main__":
    app.run(port=2222,debug=True)
