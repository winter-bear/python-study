#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Comment
from bs4 import UnicodeDammit
from bs4 import SoupStrainer
soup = BeautifulSoup(html_doc,'html.parser')
head_tag = soup.title
title_tag = soup.title

print(soup.prettify())
print(dir(soup))
print(soup.title)
print(soup.head)
print(dir(soup.title))
print(soup.title.name,soup.title.string,soup.title.parent.name,end='\n')
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.a['class'])
print(soup.a['href'])
print(soup.find_all('a'))
for i in soup.find_all('a'):
	print(i)
for i in soup.find_all('p'):
	print(i)
	print('*'*20)
print(soup.find(id="link3"))
print(soup.find(id="link3")['href'])

for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())

print(soup.head)
print(soup.head.contents)
print(type(soup.head.contents))
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.contents[0])
print(soup.head.contents[0].contents)
print(soup.head.title == soup.head.contents[0])

print(len(soup.contents))
print(soup.contents[1])
print(soup.contents[1].name)

for child in soup.p.children:
	print(child)

print(head_tag.contents)
for child in head_tag.descendants:
	print(child)
print(len(list(soup.descendants)))
print(head_tag.string)

for string in soup.strings:
	print(string)

for string in soup.stripped_strings:
    print(repr(string))
print(len(list(soup.stripped_strings)))

print(title_tag)
print(title_tag.parent)

link =soup.a
print(link)
for parent in link.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>",'lxml')
#print(sibling_soup.prettify())
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)

link = soup.a
#print(link)
#print(link.next_sibling)
#print(link.next_sibling.next_sibling)
#for sibling in soup.a.next_siblings:
    ##print(repr(sibling))
#for sibling in soup.find(id="link3").previous_siblings:
    ##print(repr(sibling))
last_a_tag = soup.find("a", id="link3")
#print(last_a_tag)
#print(last_a_tag.next_sibling)
#print(last_a_tag.next_element)
#print(last_a_tag.previous_element)
#print(last_a_tag.previous_element.next_element)
#print(last_a_tag.previous_element.next_element.next_element)
#for element in last_a_tag.next_elements:
    #print(repr(element))

#for tag in soup.find_all(re.compile("a")):
    #print(tag.name)
#for ab in soup.find_all(['a','b','p']):
	#print(ab)
#for tag in soup.find_all(True):
    #print(tag.name)
#def has_class_but_no_id(tag):
    #return tag.has_attr('class') and  not tag.has_attr('id')
#for p in soup.find_all(has_class_but_no_id):
	#print(p)

#print(soup.find_all(has_class_but_no_id))

def not_lacie(href):
        return href and not re.compile("lacie").search(href)
a=soup.find_all(href=not_lacie)
print(a)

import re
#def surrounded_by_strings(tag):
    #return (isinstance(tag.next_element, NavigableString)
            #and isinstance(tag.previous_element, NavigableString))

#for tag in soup.find_all(surrounded_by_strings):
    #print(tag.name)
#print(soup.find_all('title'))
#print(soup.find_all("p", "title"))
#print(soup.find_all("a"))
#print(soup.find_all(id="link2"))
#print(soup.find(string=re.compile("sisters")))
#print(soup.find_all(href=re.compile("elsie")))
#print(soup.find_all(id=True))
#print(soup.find_all(href=re.compile("elsie"), id='link1'))
#print(soup.find_all('a','href'))
#data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
#data_soup.find_all(data-foo="value")
#print(data_soup.find_all(attrs={"data-foo": "value"}))
#print(soup.find_all('a',class_='sister'))
#print(soup.find_all(class_=re.compile("itl")))
#def has_six_characters(css_class):
	#return css_class is not None and len(css_class) == 5
#print(soup.find_all(class_=has_six_characters))
#print(soup.find_all(attrs={'class':'sister'}))
#print(soup.find_all(string='Elsie'))
#def is_the_only_string_within_a_tag(s):
	#return(s != s.parent.string)
#print(soup.find_all(string= is_the_only_string_within_a_tag))
#print(soup.title)
#a_string = soup.find(string='Lacie')
#print(a_string)
#first_link = soup.a
#print(first_link)
#print(first_link.find_previous("p"))
#print(soup.select('title'))
tag = soup.b
new_comment = soup.new_string("Nice to see you.", Comment)
tag.append(new_comment)
print(tag,tag.contents)
new_tag = soup.new_tag('a',herf='http://www.example.com')
original_tag = BeautifulSoup("<b></b>").b
original_tag.append(new_tag)
print(original_tag)
new_tag.string = 'Link Text'
print(new_tag)
print(original_tag)

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,'lxml')
tag = soup.a
tag.insert(0,'but did not endorse')
print(tag)

soup = BeautifulSoup("<b>stop</b>")
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_before(tag)
print(soup.b)
soup.b.i.insert_after(soup.new_string('ever'))
print(soup.b)

markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup  = BeautifulSoup(markup,'lxml')
print(soup.get_text())
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit.unicode_markup)
print(dammit.original_encoding)

only_a_tags = SoupStrainer("a")

only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(string):
    return len(string) < 10

only_short_strings = SoupStrainer(string=is_short_string)
#print(BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tags).prettify())
#print(BeautifulSoup(html_doc, "html.parser", parse_only=only_tags_with_id_link2).prettify())
print(BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings).prettify())


from bs4 import BeautifulSoup
from bs4 import element
import re
#html为解析的页面获得html信息,为方便讲解，自己定义了一个html文件

html = """
<html>
<head>
<title>Jack_Cui</title>
</head>
<body>
<p class="title" name="blog"><b>My Blog</b></p>
<li><!--注释--></li>
<a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
</body>
</html>
"""
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
print(soup.title)
print(soup.li)
print(soup.li.name)
print(soup.name)
print(soup.title.string)
print(soup.a.attrs)
print(soup.a.string)
print(soup.body.contents)
for child in soup.body.children:
	print(child)
print(soup.find_all('a')
for tag in soup.find_all(True):
     print(tag.name)


# -*- coding:UTF-8 -*-
# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == "__main__":
    #创建txt文件
    file = open('一念永恒.txt', 'w', encoding='utf-8')
    #一念永恒小说目录地址
    target_url = 'http://www.biqukan.com/1_1094/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档树,找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    #计算章节个数
    numbers = (len(download_soup.dl.contents) - 1) / 2 - 8
    index = 1
    #开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
    begin_flag = False
    #遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        #滤除回车
        if child != '\n':
            #找到《一念永恒》正文卷,使能标志位
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
            #爬取链接并下载链接内容
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_req = request.Request(url = download_url, headers = head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk','ignore')
                download_name = child.string
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
                soup_text = BeautifulSoup(str(texts), 'lxml')
                write_flag = True
                file.write(download_name + '\n\n')
                #将爬取内容写入文件
                for each in soup_text.div.text.replace('\xa0',''):
                    if each == 'h':
                        write_flag = False
                    if write_flag == True and each != ' ':
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
                file.write('\n\n')
                #打印爬取进度
                sys.stdout.write("已下载:%.3f%%" % float(index/numbers) + '\r')
                sys.stdout.flush()
                index += 1
    file.close()
'''
# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import collections
import re
import os
import time
import sys
import types

"""
类说明:下载《笔趣看》网小说: url:http://www.biqukan.com/

Parameters:
	target - 《笔趣看》网指定的小说目录地址(string)

Returns:
	无

Modify:
	2017-05-06
"""
class download(object):
	def __init__(self, target):
		self.__target_url = target
		self.__head = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',}

	"""
	函数说明:获取下载链接

	Parameters:
		无

	Returns:
		novel_name + '.txt' - 保存的小说名(string)
		numbers - 章节数(int)
		download_dict - 保存章节名称和下载链接的字典(dict)

	Modify:
		2017-05-06
	"""
	def get_download_url(self):
		charter = re.compile(u'[第弟](.+)章', re.IGNORECASE)
		target_req = request.Request(url = self.__target_url, headers = self.__head)
		target_response = request.urlopen(target_req)
		target_html = target_response.read().decode('gbk','ignore')
		listmain_soup = BeautifulSoup(target_html,'lxml')
		chapters = listmain_soup.find_all('div',class_ = 'listmain')
		download_soup = BeautifulSoup(str(chapters), 'lxml')
		novel_name = str(download_soup.dl.dt).split("》")[0][5:]
		flag_name = "《" + novel_name + "》" + "正文卷"
		numbers = (len(download_soup.dl.contents) - 1) / 2 - 8
		download_dict = collections.OrderedDict()
		begin_flag = False
		numbers = 1
		for child in download_soup.dl.children:
			if child != '\n':
				if child.string == u"%s" % flag_name:
					begin_flag = True
				if begin_flag == True and child.a != None:
					download_url = "http://www.biqukan.com" + child.a.get('href')
					download_name = child.string
					names = str(download_name).split('章')
					name = charter.findall(names[0] + '章')
					if name:
							download_dict['第' + str(numbers) + '章 ' + names[1]] = download_url
							numbers += 1
		return novel_name + '.txt', numbers, download_dict
	
	"""
	函数说明:爬取文章内容

	Parameters:
		url - 下载连接(string)

	Returns:
		soup_text - 章节内容(string)

	Modify:
		2017-05-06
	"""
	def Downloader(self, url):
		download_req = request.Request(url = url, headers = self.__head)
		download_response = request.urlopen(download_req)
		download_html = download_response.read().decode('gbk','ignore')
		soup_texts = BeautifulSoup(download_html, 'lxml')
		texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
		soup_text = BeautifulSoup(str(texts), 'lxml').div.text.replace('\xa0','')
		return soup_text

	"""
	函数说明:将爬取的文章内容写入文件

	Parameters:
		name - 章节名称(string)
		path - 当前路径下,小说保存名称(string)
		text - 章节内容(string)

	Returns:
		无

	Modify:
		2017-05-06
	"""
	def Writer(self, name, path, text):
		write_flag = True
		with open(path, 'a', encoding='utf-8') as f:
			f.write(name + '\n\n')
			for each in text:
				if each == 'h':
					write_flag = False
				if write_flag == True and each != ' ':
					f.write(each)
				if write_flag == True and each == '\r':
					f.write('\n')			
			f.write('\n\n')

if __name__ == "__main__":
	print("\n\t\t欢迎使用《笔趣看》小说下载小工具\n\n\t\t作者:Jack-Cui\t时间:2017-05-06\n")
	print("*************************************************************************")
	
	#小说地址
	target_url = str(input("请输入小说目录下载地址:\n"))

	#实例化下载类
	d = download(target = target_url)
	name, numbers, url_dict = d.get_download_url()
	if name in os.listdir():
		os.remove(name)
	index = 1

	#下载中
	print("《%s》下载中:" % name[:-4])
	for key, value in url_dict.items():
		d.Writer(key, name, d.Downloader(value))
		sys.stdout.write("已下载:%.3f%%" %  float(index/numbers) + '\r')
		sys.stdout.flush()
		index += 1	

	print("《%s》下载完成！" % name[:-4])

	
