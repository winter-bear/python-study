#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import http.client  
import hashlib  
import json  
import urllib  
import random  
  
def baidu_translate(content):  
    appid = '20151113000005349'  
    secretKey = 'osubCEzlGjzvw8qdQc41'  
    httpClient = None  
    myurl = '/api/trans/vip/translate'  
    q = content  
    fromLang = 'en' # 源语言  
    toLang = 'zh'   # 翻译后的语言  
    salt = random.randint(32768, 65536)  
    sign = appid + q + str(salt) + secretKey  
    sign = hashlib.md5(sign.encode()).hexdigest()  
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(  
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(  
        salt) + '&sign=' + sign  
  
    try:  
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')  
        httpClient.request('GET', myurl)  
        # response是HTTPResponse对象  
        response = httpClient.getresponse()
        print(response)  
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        print(jsonResponse)  
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        print(js)  
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果  
        print(dst) # 打印结果  
    except Exception as e:  
        print(e)  
    finally:  
        if httpClient:  
            httpClient.close()  
  
if __name__ == '__main__':  
    while True:  
        print("请输入要翻译的内容,如果退出输入q")  
        content = input()  
        if (content == 'q'):  
            break  
        baidu_translate(content)
'''
百度翻译
import http
import hashlib
import urllib.request
import random
import json

while True:
    fin = open(r'D:\1.txt', 'r')               #以读的方式打开输入文件  
    fout = open(r'D:\2.txt', 'w')             #以写的方式打开输出文件
    for eachLine in fin:
        appid = '自己申请'    #参考百度翻译后台，申请appid和secretKey
        secretKey = '自己申请'
        httpClient = None
        myurl = '/api/trans/vip/translate'
        q = eachLine.strip()                   #文本文件中每一行作为一个翻译源
        fromLang = 'zh'                         #中文
        toLang = 'en'                             #英文
        salt = random.randint(32768, 65536)
        sign = appid+q+str(salt)+secretKey
        sign = sign.encode('UTF-8')
        m1 = hashlib.md5()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        html= response.read().decode('UTF-8')
        target2 = json.loads(html)
        src = target2["trans_result"][0]["dst"]
        #print(src)#取得翻译后的文本结果,测试可删除注释  
        outStr = src  
        fout.write(outStr.strip() + '\n')  
    fin.close()  
    fout.close()
    print('翻译成功，请查看文件')
    break
‘’‘

