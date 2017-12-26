# -*- coding:utf-8 -*-
import math
import requests
import imgutil
import time

# image save path
path = "/path/to/save"
imgutil.mkdir(path)

url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

# parameters
query = "キーワード"
count = 50      # 1リクエストあたりの最大取得件数 default:30 max:150
mkt = "ja-JP"   # 取得元の国

num_per = 10    # リクエスト回数（count * num_per=取得画像数）
offset = math.floor(count / num_per)    # ループ回数

subscriptionKey="xxxxxxxxxxxxxxxxxxx"    # Bing Search API Key

headers = {'Ocp-Apim-Subscription-Key':subscriptionKey}

for offset_num in range(offset):
    params = {'q':query,'count':count,'offset':offset_num*offset,'mkt':mkt}
    r = requests.get(url,headers=headers,params=params)
    data = r.json()
    for values in data['value']:
        image_url = values['contentUrl']
        try:
            imgutil.download_img(path,values['contentUrl'])
        except Exception as e:
            print("failed to download image at {}".format(image_url))
            print(e)
            continue
    time.sleep(1)
