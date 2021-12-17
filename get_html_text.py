from requests_html import HTMLSession

session = HTMLSession();
url = 'http://www.ohtashp.com/topics/takarakuji/'
# 把对应的网页内容 取回来
r = session.get(url)
# 只看字符串
#print(r.html.text)]
# 查看绝对链接
# print(r.html.absolute_links)
sel = 'body > div:nth-child(4) > div.table-responsive > table'
results = r.html.find(sel)
print(results)
print(results[0].text)
#print(results[0].absolute_links)
print(list(results[0].absolute_links)[0])

sel = list(results[0].absolute_links)[0]
results = r.html.find(sel)
print(results)
print(results[0].text)

def get_text_link_from_sel() :
    myList = []
    try:
        results = r.html.find(sel)
        for result in results :
            myText = result.text
            myLink = list(result.absolute_links)[0]
            myList.append(myText,myLink)
        return myList
    except:
        return None