#！/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    #对应上图的Request URL
    Request_URL = 'http://fanyi.baidu.com/v2transapi'
    #创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['from'] = 'en'
    Form_Data['to'] = 'zh'
    Form_Data['query'] = 'zhouqi'
    Form_Data['transtype'] = 'enter'
    Form_Data['simple_means_flag'] = '3'

    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
    #找到翻译结果
    ##translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译信息
    print("翻译的结果是：%s" % translate_results)
