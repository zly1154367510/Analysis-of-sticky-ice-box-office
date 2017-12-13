#!/usr/bin/env Python
# coding=utf-8
import sys
reload( sys )
sys.setdefaultencoding('utf-8')
import pandas as pd
import re
df = pd.read_csv("title.csv",encoding="GB18030");
str = ""
clearList = []
clearDf=pd.DataFrame(columns=["value"])
c = 1
ziString = "大皇帝页游新区入口"
for i in df["title"]:
    print "读取第"+`c`+"数据"
    c = i.find(ziString)
    print c
    if c == -1:
        clearList.append(i)
    else:
        continue

for i in clearList:
    str += i
str1 = str.replace(" ","")
file = open("content.txt","w");
file.write(str1)
file.close()