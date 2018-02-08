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
head = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19',}

def fm_getdata(page_num,html):
	down_url= html+'='+str(page_num)
	dow_req = request.Request(url=down_url,headers=head)
	down_response = request.urlopen(dow_req)
	down_html = down_response.read().decode('utf-8','ignore')
	html_soup = BeautifulSoup(down_html,'lxml')
	regex1 = re.compile('<div class=".*? 固件标题">(.*?)</div>',re.S)
	regex2 = re.compile('<div class=".*? 固件密码">(.*?)</div>',re.S)
	regex3 = re.compile('<div class=".*? 下载链接">\n?<a href="(.*?)"',re.S)
	name_text = re.findall(regex1,str(html_soup))
	psswd_text = re.findall(regex2,str(html_soup))
	downlink_text = re.findall(regex3,str(html_soup))
	num_pagefm = len(name_text)
	return name_text,psswd_text,downlink_text,num_pagefm	

def writer(page_num,path,name,text):
	with open(path,'a',encoding='utf-8') as f:
		print('获取第%2d页固件链接：'%page_num)
		f.write("{:^50}".format(name)+'\t')
		f.write("{:<60}".format(text)+'\n')

if __name__ == '__main__':
	txt_name = str(input('请输入要保存的文档名称：\n'))+'.txt'
	page_num = int(input('请输入要扒的固件页码最大数：\n'))
	num_fm = 0
	text = []
	index = 1
	for  i in range(1,page_num+1):
		data = fm_getdata(i,html=web)
		name,psswd,downlink,num=data
		num_fm = num_fm+num
		if name:
			for j in range(0,num):
				text = downlink[j]+'\t'+psswd[j]
				writer(i,txt_name,name[j],text)
	print('固件链接扒取完毕，总计%d个固件链接' %num_fm)







