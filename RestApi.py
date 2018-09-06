# coding =utf-8

import requests

host = 'http://192.168.100.214:3000'

class RestApi:

  def create_user(self, data):
    r = requests.post(host + '/api/v1/dc/users', data=data)
    print(r.text)

  def create_video(self, id, name):
    d = {'name': name, 'id': id}
    r = requests.post(host + '/data_videos', data=d)
    print(r.text)
