import requests
import pandas as pd
from bs4 import BeautifulSoup
#from lxml import etree
#import time
#from time import sleep
url = 'http://quote.fx678.com/exchange/WH'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.content)
item_list=soup.find_all('td')#找到网页表格中的所有内容
num=len(item_list)
print(num)

names=[]                  #存放外汇产品的名称
price_new=[]              #外汇产品的最新价格
price_change=[]           #外汇产品涨跌值
price_percentage=[]       #外汇产品的涨跌幅度
price_high=[]             #外汇产品当日最高价
price_low=[]              #外汇产品当日最低价
price_yesterday=[]        #外汇产品昨日收盘价
time_update=[]            #更新时间

for i in range(0,num,8):#从0位置开始，每隔7个位置就是产品名称
    names.append(item_list[i].text)

for i in range(1,num,8):#从1位置开始，每隔7个位置就是产品j价格
    price_new.append(item_list[i].text)

for i in range(2,num,8):#从2位置开始，每隔7个位置就是产品涨跌值
    price_change.append(item_list[i].text)

for i in range(3,num,8):#从3位置开始，每隔7个位置就是产品涨跌幅度
    price_percentage.append(item_list[i].text)

for i in range(4,num,8):#从4位置开始，每隔7个位置就是产品当日最高价
    price_high.append(item_list[i].text)

for i in range(5,num,8):#从5位置开始，每隔7个位置就是产品当日最低价
    price_low.append(item_list[i].text)

for i in range(6,num,8):#从6位置开始，每隔7个位置就是产品昨日收盘时价
    price_yesterday.append(item_list[i].text)

for i in range(7,num,8):#从7位置开始，每隔7个位置就是产品价格更新时间
    time_update.append(item_list[i].text)

item_dict={'names':names,'price_new':price_new,'price_change':price_change,'price_percentage':price_percentage,'price_high':price_high,\
      'price_low':price_low,'price_yesterday':price_yesterday,'time_update':time_update}
    

df=pd.DataFrame(item_dict)
df.to_csv('waihui.csv')