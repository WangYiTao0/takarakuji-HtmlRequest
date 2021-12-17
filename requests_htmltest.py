from requests_html import HTMLSession
import numpy as np
session = HTMLSession();
url = 'http://www.ohtashp.com/topics/takarakuji/'
# 把对应的网页内容 取回来
r = session.get(url)
# 只看字符串
#print(r.html.text)]
# 查看绝对链接
# print(r.html.absolute_links)
# selector
index = 153
sel = 'body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1)'
last = 'body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(153)'

 #results = r.html.find(sel)
 #print(type(results))
 #print(results)
# print(results[0].text)
# print(list(results[0].absolute_links)[0])
#'body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(53) <tr> 390'

# 52 开始有问题 52 包含了下面所有的表格信息
sel = 'body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(51)'
sel1 = 'body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1) > th'
# body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1)
# body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1) > th
# body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2)
# body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1) > td.hon.c02
# body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1) > td.hon.c21
print(sel)
results = r.html.find(sel)
#print(results)
#print(results[0].text)

print(results[0].text[0])
print(results[0].text[1])
print(results[0].text[2])
print(results[0].text[3])
print(results[0].text[4])
print(results[0].text[5])
print(results[0].text[6])
print(type(results[0].text))
# print(results[0].text[results[0].text.count])

numDic = {"":""}

# for i in range(51) :
#     strIndex = str(i + 1)
#     print(strIndex)
#     sel = 'body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(' + strIndex + ')'
#     print(sel)
#     results = r.html.find(sel)
#     print(results[0].text)
#     numDic[results[0].text[0]] =
