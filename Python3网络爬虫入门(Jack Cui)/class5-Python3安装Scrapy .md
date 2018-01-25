 Python3网络爬虫(五)：Python3安装Scrapy

转载请注明作者和出处：http://blog.csdn.net/c406495762/article/details/60156205

一、Scrapy简介

  Scrapy是一个为了爬取网站数据提取结构性数据而编写的应用框架，可以应用于数据挖掘，信息处理或存储历史数据等一些列的程序中。Scrapy最初就是为了网络爬取而设计的。现在，Scrapy已经推出了曾承诺过的Python3.x版本。

  为什么学习Scrapy呢？它能我们更好的完成爬虫任务，自己写Python爬虫程序好比孤军奋战，而使用了Scrapy就好比手底下有了千军万马。Scrapy可以起到事半功倍(甚至好几倍*.*)的效果。所以，学习Scrapy也就显得很有必要了。

二、Scrapy安装

  1.直接使用指令pip3 install scrapy，发现有诸多错误。

  Failed building wheel for lxml
  Microsoft Visual C++ 10.0 is required
  Failed building twisted
  Unable to find vcvarsall.bat

  遇到的错误，如下图所示：

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-1.png)

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-2.png)

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-3.png)

2.解决办法

  在http://www.lfd.uci.edu/~gohlke/pythonlibs/有很多用于windows的编译好的Python第三方库，我们下载好对应自己Python版本的库即可。

  (1)在cmd中输入指令python，查看python的版本，如下：

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-4.png)

  从上图可以看出可以看出我的Python版本为Python3.5.2-64bit。

  (2)登陆http://www.lfd.uci.edu/~gohlke/pythonlibs/，Ctrl+F搜索Lxml、Twisted、Scrapy，下载对应的版本，例如：lxml-3.7.3-cp35-cp35m-win_adm64.whl，表示lxml的版本为3.7.3，对应的python版本为3.5-64bit。我下载的版本如下图所示：

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-5.png)

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-6.png)

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-7.png)

  (3)在cmd中输入DOS指令，进入下载好的whl文件夹下，例如我的三个whl文件放在了Scrapy文件夹下：

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-8.png)

  (4)依次执行如下命令：

   a.pip3 install wheel

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-9.png)

   b.pip3 install lxml-3.7.3-cp35-cp35m-win_amd64.whl

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-10.png)

   c.pip3 install Twisted-17.1.0-cp35-cp35m-win_amd64.whl

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-11.png)

   d.pip3 install Scrapy-1.3.2-py2.py3-none-any.whl

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-12.png)

  这样Scrapy的安装就完成了，请忽略最后两行让我升级pip的信息。*.*

  (5)Srapy已经安装成功，还要下载pywin32，找到对应版本下载，一路下一步安装即可。安装完成后，就可以正常使用Scrapy了。

  URL：https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/

![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-13.png)

  至此，大功告成，我们可以愉快的使用Scrapy了。
![image](https://github.com/winter-bear/python-study/blob/master/Python3%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8(Jack%20Cui)/screenshot/5-14.png)