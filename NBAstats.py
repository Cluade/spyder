#引入主要的爬取工具：
import requests
from bs4 import BeautifulSoup

#一下是数据的清洗和存储所需要的辅助工具
import re
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

def fillframe(tbody,index):   #这里只使用tbody标签，表头通过index传入，index是一个list
    frame=DataFrame()
    if tbody:
        all_tr=tbody.find_all('tr')
        for tr in all_tr:
            dic={}
            all_td=tr.find_all('td')
            i=-1
            for td in all_td:
                if i==-1:    #可以发现，网页表格中每行的第一格都是空的，所以我们需要将其跳过。
                    i+=1
                    continue
                else:
                    dic[index[i]]=td.string
                i+=1
            frame=pd.concat([frame,DataFrame(dic,index=[0])],ignore_index=True)
        return frame

def fillindex(thead):
    index=[]
    if thead:
        all_th=thead.tr.find_all('th')
        i=-1
        for th in all_th:
            if i==-1:
                i+=1
                continue
            else:
                index.append(th.string)
            i+=1
        return index

index=['球员','赛季','结果','比分','首发','时间','投篮','命中','出手','三分',
        '三分命中','三分出手','罚球','罚球命中','罚球出手',
        '篮板','前场','后场','助攻','抢断','盖帽'
        ,'失误','犯规','得分']

def spider(page,player_id,gametype,index):
    url='http://www.stat-nba.com/query.php?page='+str(page)+'&QueryType=game&GameType='+str(gametype)+'&Player_id='+str(player_id)+'&crtcol=season&order=1'
    r=requests.get(url,timeout=30)
    if r.status_code==200:
        demo=r.text
        soup=BeautifulSoup(demo,"html.parser")

        data=soup.find('div',{'class':'stat_box'})
        if not data:           #找不到数据表格时退出
            return False

        table=data.find('table')
        if table:
            tbody=table.find('tbody')
            return fillframe(tbody,index)
        else:    #数据表格为空时退出
            return False
    else:   #页面读取失败时退出
        return False

def update(frame,path,filename):
    try:  #尝试读取文件filename
        frame0=pd.read_csv(path)
    except: #如果文件已经存在，则更新它
        frame.to_csv(path)
    else: #否则创建名为filename的文件
        frame0=pd.concat([frame0,frame],ignore_index=True)
        frame0.to_csv(path)
frame_player=DataFrame()
gametype='season'

for player_id in range(1862,1863):  #这里仅爬取一位球员（James）测试，需要正式爬取请改为range(1,4450)
    page=0
    flag=True
    while flag:
        result=spider(page,player_id,gametype,index)
        if type(result)==bool and not result:   #返回False时
            flag=False
            break
        else:   #爬取成功时读取表格
            frame_player=pd.concat([frame_player,result],ignore_index=True)
        update(frame_player,'LBJ.csv','LBJ.csv')
        print(page)
        page+=1
