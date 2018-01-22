#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
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

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.51cube.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        # html = responese.read()
    except error.HTTPError as e:
        print(e.code)
'''
if __name__ == "__main__":
	url = "http://www.51cube.com/Jack_Cui.html"
	req = request.Request(url)
	try:
		responese = request.urlopen(req)
	except error.URLError as e:
		if hasattr(e,"code"):
			print("HTTPError")
			print(e.code)
		elif hasattr(e,"reason"):
			print("URLError")
			print(e.reason)