#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request  
response = request.urlopen(r'http://www.baidu.com/')  
html = response.read()  
filebaidu = open('baidu.html','wb+')
filebaidu.write(html)
filebaidu.close
