#import libs
import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

import sys
import time

# reload(sys)
# sys.setdefaultencoding('utf-8')

client = MongoClient('localhost',27017)
db = client.riche
collection = db.riche_collect


link = "https://tieba.baidu.com/p/4877675324"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


r = requests.get(link,headers=headers)

soup = BeautifulSoup(r.text,"lxml")

content_list = soup.find_all("div",class_ = "d_post_content j_d_post_content ")
for i in range(len(content_list)):
    conent = content_list[i].text.strip()
    print ("诗集"+str(i+1)+":")
    print (conent)
    post = {
        "id":i,
        "content":conent,
        "date":datetime.datetime.utcnow()#获取当前时间
    }
    collection.insert_one(post)