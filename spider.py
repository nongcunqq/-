# coding:utf-8

# 引入相关模块
import requests, urllib, time
from bs4 import BeautifulSoup

from lxml import etree

proxies = {
    "http" : "http://192.168.1.21:1087"
}

url = "http://www.westca.com/Yellow_Pages/place/place=0/lang=schinese.html"

wbdata = requests.get(url, proxies=proxies).text
# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata,'lxml')
# 从解析文件中通过select选择器定位指定的元素，返回一个列表
two_large = soup.select("#content > table > tr > td")
#print(two_large)

three = soup.select('#sidebar > ul > li:nth-child(2) > div > select')
print(three)

tree = etree.HTML(wbdata)
# content = tree.xpath('//*[@id="content"]/table')
# print(wbdata)
# print(content)



