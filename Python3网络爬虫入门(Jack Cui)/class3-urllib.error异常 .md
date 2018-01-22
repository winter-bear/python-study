 Python3网络爬虫(三)：urllib.error异常
标签： python网络爬虫异常
2017-03-02 12:29 11956人阅读 评论(16) 收藏 举报
分类：
Python（26）

版权声明：本文为博主原创文章，未经博主允许不得转载。

运行平台：Windows
Python版本：Python3.x
IDE：Sublime text3

转载请注明作者和出处：http://blog.csdn.net/c406495762/article/details/59488464

一.urllib.error

    urllib.error可以接收有urllib.request产生的异常。urllib.error有两个方法，URLError和HTTPError。如下图所示：

    ![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/3-1.png)

    ![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/3-2.png)

    URLError是OSError的一个子类，HTTPError是URLError的一个子类，服务器上HTTP的响应会返回一个状态码，根据这个HTTP状态码，我们可以知道我们的访问是否成功。例如第二个笔记中提到的200状态码，表示请求成功，再比如常见的404错误等。

1.URLError

    让我们先看下URLError的异常，创建文件urllib_test06.py，编写如下代码：

# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error

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


    我们可以看到如下运行结果：

    ![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/3-3.png)

2.HTTPError

    再看下HTTPError异常，创建文件urllib_test07.py，编写如下代码：

# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        # html = responese.read()
    except error.HTTPError as e:
        print(e.code)


    运行之后，我们可以看到404，这说明请求的资源没有在服务器上找到，www.douyu.com这个服务器是存在的，但是我们要查找的Jack_Cui.html资源是没有的，所以抛出404异常。
    ![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/3-4.png)

二.URLError和HTTPError混合使用

    最后值得注意的一点是，如果想用HTTPError和URLError一起捕获异常，那么需要将HTTPError放在URLError的前面，因为HTTPError是URLError的一个子类。如果URLError放在前面，出现HTTP异常会先响应URLError，这样HTTPError就捕获不到错误信息了。

    ![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/3-5.png)

    如果不用上面的方法，也可以使用hasattr函数判断URLError含有的属性，如果含有reason属性表明是URLError，如果含有code属性表明是HTTPError。创建文件urllib_test08.py，编写代码如下：

# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
    except error.URLError as e:
        if hasattr(e, 'code')
            print("HTTPError")
            print(e.code)
        elif hasattr(e, 'reason')
            print("URLError")
            print(e.reason)


    运行结果如下：

    ![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/3-6.png)
