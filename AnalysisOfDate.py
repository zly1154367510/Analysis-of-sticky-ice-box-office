#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("GB18030")
import pandas as pd
from bs4 import BeautifulSoup as bfl
import urllib2
import re
class tieStr:
    def __init__(self,lz,replieser):
        self.lz = lz
        self.replieser = replieser



url = "https://bbs.hupu.com/bxj-";
start = 1
urlStart = 1
tieurlLiss = []
tieTitleList = []
tiepeliseList = []
tieContentList = []
tieStrUrlList = []
titleDf = pd.DataFrame(columns=['title'])


import random

my_headers=[
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]
def writeFile(title,value):
    fileloca = open(title,"w")
    fileloca.write(value)
    fileloca.close()

str = ""
while start<11:


    page = start
    print "正在抓取第"+`page`+"个页面url"
    random_headers = random.choice(my_headers)
    headers = {'User-Agent': random_headers}
    requset = urllib2.Request(headers=headers,url=url+`start`)
    start += 1
    content = urllib2.urlopen(requset).read()
    soup = bfl(content,"html.parser")
    '''
    tieurls：匹配的帖子url父类
    tieurllist：帖子的url列表
    '''
    tieurls = soup.find_all("div",{"class","titlelink box"})
    for i in tieurls:
        print i.a.get('href')
        tieurlLiss.append(i.a.get('href'))
        urlStart += 1

tieStrat = 0
str1 = ""
str2 = ""
for i in tieurlLiss:
    random_headers = random.choice(my_headers)
    headers = {'User-Agent': random_headers}
    tieStrat+=1
    print "正在抓取第"+`tieStrat`+"个帖子内容"
    request = urllib2.Request(headers=headers,url="https://bbs.hupu.com"+i)
    content = urllib2.urlopen(request).read()
    soup = bfl(content,"html.parser")
    # file = open("content.txt","w")
    # file.write(content);
    # file.close()
    '''
    tieTitle：匹配标题文本内容
    tieTitleList：文本内容
    1
    '''

    tieTitle = soup.find_all("div",{"class","subhead"})
    for i in tieTitle:
        print i.span.text

        str +=i.span.text
    writeFile("title.txt",str)
    '''
    获取个人用户URL
    2
    '''
    # tieStrList = soup.find_all("a",{"class","headpic"})
    # for i in tieStrList:
    #     print i.get("href")
    #     tieStrUrlList.append(i.get("href"))

    '''
    获取lz内容内容
    3
    '''
    tieContent = soup.find_all("div",{"class","quote-content"})
    for i in tieContent:
        print i.text

        str2 += i.text
    writeFile("lzContent.txt", str)

    '''
    获取JRS评论内容
    4
    '''

    tiePelise = soup.find_all("table",{"class","case"})
    for i in tiePelise:
        print i.text

        str1 += i.text
    writeFile("pelies.txt", str)


print "正在写入"
# titleDf["title"] = tieStrUrlList
# titleDf.to_csv("title.csv")


print "完成"