#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import urllib
import os  
response = request.urlopen(r'http://www.baidu.com/')  
html = response.read()  
with open('baidu.html','wb') as f:
    f.write(html)
'''	
url1 = 'http://www.someserver.com/register.cgi'
values = {'name' : 'WHY',    
          'location' : 'SDU',    
          'language' : 'Python' }
data1 = urllib.encode(values)
req1 = request(url1,data1)
response = urllib.urlopen(req1)
the_page = response.read()

data = {}
data['name']= 'why'
data['location']= 'SDU'
data['language']= 'python'

url_values = urllib.encode(data)
print(url_values)
name=Somebody+Here&language=Python&location=Northampton
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values 

data = urllib.open(full_url)
print(data)
'''
data = {}
data['name']= 'why'
data['location']= 'SDU'
data['language']= 'python'
url = 'http://www.baidu.com'
user_agent =  'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
headers = { 'User-Agent' : user_agent }    
##data = urllib.encode(values)        
response = request.urlopen(url,headers)    
the_page = response.read()
with open('baiduios.html','wb') as f:
    f.write(the_page)
