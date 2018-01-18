#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request 
from urllib import error
'''
if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.iloveyou.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)

req = request.Request('http://www.51cube.com/')  
  
try:  
    request.urlopen(req)  
  
except error.URLError as e:  
  
    print(e.code)  
    #print e.read()
'''
req = request.Request('http://bbs.csdn.net/callmewhy')  
  
try:  
  
    response = request.urlopen(req)  
  
except error.HTTPError as e:  
  
    print('The server couldn\'t fulfill the request.')  
  
    print('Error code: ', e.code)  
  
except error.URLError as e:  
  
    print('We failed to reach a server.')  
  
    print('Reason: ', e.reason)  
  
else:  
    print('No exception was raised.')  
    # everything is fine  
