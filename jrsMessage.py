#coding=utf-8
import pandas as pd
import random
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('GB18030')
from bs4 import BeautifulSoup

df = pd.read_csv("title.csv");
df = df.drop_duplicates()
messageDf = pd.DataFrame(columns=["加入时间"])


jrs_name_list = []
jrs_sex_list = []
jrs_region_list = []
jrs_time_to_join_list = []
my_headers=[
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]

for i in df['title']:
    random_headers = random.choice(my_headers)
    url = i;
    headers = {'User-Agent': random_headers}
    request = urllib2.Request(headers = headers,url=url)

    content = urllib2.urlopen(request).read()

    soup = BeautifulSoup(content,"html.parser")
    jrs_name = soup.find_all("div",{"class","left"})
    '''
    获取虎扑ID
    '''
    # for i in jrs_name:
    #     print i.text
    #     jrs_name_list.append(i.text)
    '''
    获取jrs性别
    '''
    jrs_time_to_join = soup.find_all("div",{"class","personalinfo"})
    print "虫子开始爬"
    for i in jrs_time_to_join:
        print re.findall(re.compile("加入时间"),i.text)




