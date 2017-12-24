# -*- coding:utf-8 -*-
import urllib.request
import httplib2
import os
import base64
import hashlib
import sha3
import imgutil
from googleapiclient.discovery import build

# image save path
path = "/path/to/save"

# parameters
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
cse_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
query = "キーワード"
service = build("customsearch","v1",developerKey=api_key)

imgutil.mkdir(path)

page_limit = 10 # 検索ページ数
startIndex = 1
response = []
img_list = []

for nPage in range(0,page_limit):
    print("reading page number:",nPage + 1)
    try:
        response.append(service.cse().list(
            q=query,
            cx=cse_key,
            lr="lang_ja",
            num=10,
            start=startIndex,
            searchType="image"
        ).execute())
        startIndex = response[nPage].get("queries").get("nextPage")[0].get("startIndex")
    except Exception as e:
        print(e)

for i in range(len(response)):
    if len(response[i]['items']) > 0:
        for j in range(len(response[i]['items'])):
            img_list.append(response[i]['items'][j]['link'])

for i in range(len(img_list)):
    http = httplib2.Http(".cache")
    url = img_list[i]
    try:
        imgutil.download_img(path,url)
    except Exception as e:
        print("failed to download image at {}".format(url))
        print(e)
        continue
