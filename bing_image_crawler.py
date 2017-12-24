# -*- coding:utf-8 -*-
import math
import requests
import json
import urllib
import os
import imgutil

path = "/path/to/img"
img_dir = os.path.join(path,"dlib")
imgutil.mkdir(img_dir)

url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

query = "キーワード"
count = 50
num_per = 50 #default:30 max:150
offset = math.floor(count / num_per)
mkt = "ja-JP"

SubscriptionKey="xxxxxxxxxx"
api="xxxxxxxxxxxxxx"

headers = {SubscriptionKey:api}

for offset_num in range(offset):
    params = {'q':query,'count':count,'offset':offset_num*offset,'mkt':mkt}
    r = requests.get(url,headers=headers,params=params)
    data = r.json()
    for values in data['value']:
        image_url = values['contentUrl']
        try:
            imgutil.download_img(img_dir,values['contentUrl'])
        except Exception as e:
            print("failed to download image at {}".format(image_url))
            print(e)
            continue
