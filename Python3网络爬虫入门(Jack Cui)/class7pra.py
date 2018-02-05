from urllib import request
from bs4 import BeautifulSoup
download_req = request.Request(url = 'http://www.biqukan.com/2_2910/1272110.html')
download_response = request.urlopen(download_req)
download_html = download_response.read().decode('gbk','ignore')
soup_texts = BeautifulSoup(download_html, 'lxml')
texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
soup_text = BeautifulSoup(str(texts), 'lxml').div.text.replace('\xa0','')
'''
with open('a.txt','w', encoding='utf-8') as f:
	for each in soup_text:
		f.write(each)
'''