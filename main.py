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
sel = 'body > div:nth-child(4) > div.table-responsive > table > tbody > tr:nth-child(1)'
results = r.html.find(sel)
print(type(results))
print(results)
print(results[0].text)
#print(list(results[0].absolute_links)[0])




#print(results)