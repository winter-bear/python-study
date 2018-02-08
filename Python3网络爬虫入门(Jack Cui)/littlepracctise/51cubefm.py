#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import collections
import re
import os
import time
import sys
import types
web = 'http://51cube.com/services?_page'
def downloadcubefm(page,txt_name):
	p = 1
	while p <= page+1:
		down_url = web+'='+str(p)
		head = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',}
		down_req = request.Request(url=down_url,headers=head)
		down_response = request.urlopen(down_req)
		down_html = down_response.read().decode('utf-8','ignore')
		html_soup=BeautifulSoup(down_html,'lxml')
		name = html_soup.find_all('div',class_=re.compile('固件标题'))
		if name:
			with open(txt_name,'a',encoding = 'utf-8') as f:
				#name =  html_soup.find_all('div',class_=re.compile('固件标题'))
				#name_text = list(BeautifulSoup(str(name),'lxml').strings)[1:-1][0::2]
				#psswd = html_soup.find_all('div',class_=re.compile('固件密码'))
				#psswd_text = list(BeautifulSoup(str(psswd),'html.parser').stripped_strings)[1:-1]
				#psswd_text = ['None' if x == ',' else x for x in psswd_text]
				#downlink = html_soup.find('div',class_=re.compile('下载链接'))
				#downlink_text = BeautifulSoup(str(downlink),'lxml').find_all('a')
				#regex = re.compile('href="(.*?)"')
				#downlink_text = re.findall(regex,str(downlink_text))
				regex1 = re.compile('<div class=".*? 固件标题">(.*?)</div>',re.S)
				regex2 = re.compile('<div class=".*? 固件密码">(.*?)</div>',re.S)
				regex3 = re.compile('<div class=".*? 下载链接">\n?<a href="(.*?)"',re.S)
				name_text = re.findall(regex1,str(html_soup))
				psswd_text = re.findall(regex2,str(html_soup))
				downlink_text = re.findall(regex3,str(html_soup))
				print('获取酷比的固件官网'+str(p)+'页的固件下载链接')
				f.write('\n酷比魔方官网第'+str(p)+'页固件\n'+'*'*40+'\n')
				for i in range(0,len(name_text)):
					f.write("{0:<10}\t{1:>30}\t{2:>30}".format(name_text[i],psswd_text[i],downlink_text[i],chr(12288))+'\n')
		else:
			break
		p +=1
	return print('总计有%d页固件'%(p-1))

if __name__ == "__main__":
	page = input('请输入要扒的固件页码：\n')
	txt_name = str(input('请输入要保存的文档名称：\n'))+'.txt'
	downloadcubefm(int(page),str(txt_name))
	print('保存文档完成！')	

