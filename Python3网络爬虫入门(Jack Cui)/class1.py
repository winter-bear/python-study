#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import chardet
from urllib import request
response = request.urlopen("http://fanyi.baidu.com")
html = response.read()
charset = chardet.detect(html)
print(charset)
