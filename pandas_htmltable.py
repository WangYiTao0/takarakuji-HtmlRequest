import pandas as pd
import requests
from requests_html import HTMLSession
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
url = 'http://www.ohtashp.com/topics/takarakuji/'
# ssl._create_default_https_context = ssl._create_unverified_context
#
# html = urlopen(url)
# bsObj = BeautifulSoup(html, "html.parser")
#
# # テーブルを指定
# table = bsObj.findAll("table", {"class":"tablesorter"})[0]
# rows = table.findAll("tr")
#
# with open("ebooks.csv", "w", encoding='utf-8') as file:
#     writer = csv.writer(file)
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll(['td', 'th']):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)

# 找到所需爬取的表格  [1]代表取第二个表格
# res=requests.get(url)
# res.content.decode("utf8")
dfs = pd.read_html(url)[0]
text = dfs.to_csv('kuji.csv', encoding='utf-8-sig', header=0,index=0)

#print(dfs[0])
page = requests.get(url)
page.encoding = 'utf-8'
#page.content.decode("utf-8")
text = page.content.decode()
# text = text.encode('utf-8')
#print(text)
# print(page.content.decode())
soup = BeautifulSoup(page.text, 'html.parser')
dfs = pd.read_html(page.text)
table = soup.find_all('table')[0]
# print(table)
print (table.find_all("th"))
# for child in table.children:
#     for td in child:
#         print(td.text)
# rint(dfs[0])

