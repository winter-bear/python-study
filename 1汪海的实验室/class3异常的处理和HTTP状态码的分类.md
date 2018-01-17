[Python]网络爬虫（三）：异常的处理和HTTP状态码的分类
原创 2013年05月14日 09:51:31

先来说一说HTTP的异常处理问题。
当urlopen不能够处理一个response时，产生urlError。
不过通常的Python APIs异常如ValueError,TypeError等也会同时产生。
HTTPError是urlError的子类，通常在特定HTTP URLs中产生。
 
1.URLError
通常，URLError在没有网络连接(没有路由到特定服务器)，或者服务器不存在的情况下产生。

这种情况下，异常同样会带有"reason"属性，它是一个tuple（可以理解为不可变的数组），

包含了一个错误号和一个错误信息。

我们建一个urllib2_test06.py来感受一下异常的处理：

[python] view plain copy

    import urllib2  
      
    req = urllib2.Request('http://www.baibai.com')  
      
    try: urllib2.urlopen(req)  
      
    except urllib2.URLError, e:    
        print e.reason  



按下F5，可以看到打印出来的内容是：

[Errno 11001] getaddrinfo failed

也就是说，错误号是11001，内容是getaddrinfo failed


2.HTTPError
服务器上每一个HTTP 应答对象response包含一个数字"状态码"。

有时状态码指出服务器无法完成请求。默认的处理器会为你处理一部分这种应答。

例如:假如response是一个"重定向"，需要客户端从别的地址获取文档，urllib2将为你处理。

其他不能处理的，urlopen会产生一个HTTPError。

典型的错误包含"404"(页面无法找到)，"403"(请求禁止)，和"401"(带验证请求)。

HTTP状态码表示HTTP协议所返回的响应的状态。

比如客户端向服务器发送请求，如果成功地获得请求的资源，则返回的状态码为200，表示响应成功。

如果请求的资源不存在， 则通常返回404错误。 

HTTP状态码通常分为5种类型，分别以1～5五个数字开头，由3位整数组成：

------------------------------------------------------------------------------------------------

200：请求成功      处理方式：获得响应的内容，进行处理 

201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到 

202：请求被接受，但处理尚未完成    处理方式：阻塞等待 

204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃

300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL 

304 请求的资源未更新     处理方式：丢弃 

400 非法请求     处理方式：丢弃 

401 未授权     处理方式：丢弃 

403 禁止     处理方式：丢弃 

404 没有找到     处理方式：丢弃 

5XX 回应代码以“5”开头的状态码表示服务器端发现自己出现错误，不能继续执行请求    处理方式：丢弃

------------------------------------------------------------------------------------------------
HTTPError实例产生后会有一个整型'code'属性，是服务器发送的相关错误号。

Error Codes错误码
因为默认的处理器处理了重定向(300以外号码)，并且100-299范围的号码指示成功，所以你只能看到400-599的错误号码。
BaseHTTPServer.BaseHTTPRequestHandler.response是一个很有用的应答号码字典，显示了HTTP协议使用的所有的应答号。

当一个错误号产生后，服务器返回一个HTTP错误号，和一个错误页面。

你可以使用HTTPError实例作为页面返回的应答对象response。

这表示和错误属性一样，它同样包含了read,geturl,和info方法。

我们建一个urllib2_test07.py来感受一下：

[python] view plain copy

    import urllib2  
    req = urllib2.Request('http://bbs.csdn.net/callmewhy')  
      
    try:  
        urllib2.urlopen(req)  
      
    except urllib2.URLError, e:  
      
        print e.code  
        #print e.read()  


按下F5可以看见输出了404的错误码，也就说没有找到这个页面。



3.Wrapping

所以如果你想为HTTPError或URLError做准备，将有两个基本的办法。推荐使用第二种。

我们建一个urllib2_test08.py来示范一下第一种异常处理的方案：
[python] view plain copy

    from urllib2 import Request, urlopen, URLError, HTTPError  
      
    req = Request('http://bbs.csdn.net/callmewhy')  
      
    try:  
      
        response = urlopen(req)  
      
    except HTTPError, e:  
      
        print 'The server couldn\'t fulfill the request.'  
      
        print 'Error code: ', e.code  
      
    except URLError, e:  
      
        print 'We failed to reach a server.'  
      
        print 'Reason: ', e.reason  
      
    else:  
        print 'No exception was raised.'  
        # everything is fine  


和其他语言相似，try之后捕获异常并且将其内容打印出来。
这里要注意的一点，except HTTPError 必须在第一个，否则except URLError将同样接受到HTTPError 。
因为HTTPError是URLError的子类，如果URLError在前面它会捕捉到所有的URLError（包括HTTPError ）。


我们建一个urllib2_test09.py来示范一下第二种异常处理的方案：

[python] view plain copy

    from urllib2 import Request, urlopen, URLError, HTTPError  
      
    req = Request('http://bbs.csdn.net/callmewhy')  
        
    try:    
        
        response = urlopen(req)    
        
    except URLError, e:    
      
        if hasattr(e, 'code'):    
        
            print 'The server couldn\'t fulfill the request.'    
        
            print 'Error code: ', e.code    
      
        elif hasattr(e, 'reason'):    
        
            print 'We failed to reach a server.'    
        
            print 'Reason: ', e.reason    
        
        
    else:    
        print 'No exception was raised.'    
        # everything is fine    