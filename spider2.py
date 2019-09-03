# coding:utf-8

# 引入相关模块
import requests, urllib, time
from bs4 import BeautifulSoup

proxies = {
    "http" : "http://192.168.1.21:1087"
}

url = "http://www.westca.com/Yellow_Pages/place/place=0/lang=schinese.html"

url2 = "http://www.westca.com/Yellow_Pages/place/place=83/%E7%BE%8E%E5%9B%BD%E9%BB%84%E9%A1%B5/lang=schinese.html"


#content > table > tbody > tr > td:nth-child(1)

wbdata = requests.get(url2, proxies=proxies).text
# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata,'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
two_large = soup.select("#content > div:nth-child(3)")[0].select("a")

print("len " + str(len(two_large)))

for i in two_large:
    print(i["href"])
    href = "http://www.westca.com/" + i['href'] #汉字转码
    print(href)
    l = href.split('/')
    l[-2] = urllib.parse.quote(l[-2])
    l = '/'.join(l)
    time.sleep(1)
    if '下属黄页' in wbdata:
        wbdata = requests.get(l, proxies=proxies).text
        soup = BeautifulSoup(wbdata, 'lxml')
        # 从解析文件中通过select选择器定位指定的元素，返回一个列表
        two_large = soup.select("#content > div:nth-child(3)")[0].select("a")
        time.sleep(1)
        for i in two_large:
            print(i["href"])
            href = "http://www.westca.com/" + i['href']  # 汉字转码
            print(href)
            l = href.split('/')
            l[-2] = urllib.parse.quote(l[-2])
            l = '/'.join(l)
            time.sleep(1)

    print(l)
    print(i.text)




