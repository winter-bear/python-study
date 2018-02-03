#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Comment
soup = BeautifulSoup(html_doc,'html.parser')
head_tag = soup.title
title_tag = soup.title
'''
print(soup.prettify())
print(dir(soup))
print(soup.title)
print(soup.head)
print(dir(soup.title))
print(soup.title.name,soup.title.string,soup.title.parent.name,end='\n')
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.a['class'])
print(soup.a['href'])
print(soup.find_all('a'))
for i in soup.find_all('a'):
	print(i)
for i in soup.find_all('p'):
	print(i)
	print('*'*20)
print(soup.find(id="link3"))
print(soup.find(id="link3")['href'])

for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())

print(soup.head)
print(soup.head.contents)
print(type(soup.head.contents))
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.contents[0])
print(soup.head.contents[0].contents)
print(soup.head.title == soup.head.contents[0])

print(len(soup.contents))
print(soup.contents[1])
print(soup.contents[1].name)

for child in soup.p.children:
	print(child)

print(head_tag.contents)
for child in head_tag.descendants:
	print(child)
print(len(list(soup.descendants)))
print(head_tag.string)

for string in soup.strings:
	print(string)

for string in soup.stripped_strings:
    print(repr(string))
print(len(list(soup.stripped_strings)))

print(title_tag)
print(title_tag.parent)

link =soup.a
print(link)
for parent in link.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>",'lxml')
#print(sibling_soup.prettify())
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)

link = soup.a
#print(link)
#print(link.next_sibling)
#print(link.next_sibling.next_sibling)
#for sibling in soup.a.next_siblings:
    ##print(repr(sibling))
#for sibling in soup.find(id="link3").previous_siblings:
    ##print(repr(sibling))
last_a_tag = soup.find("a", id="link3")
#print(last_a_tag)
#print(last_a_tag.next_sibling)
#print(last_a_tag.next_element)
#print(last_a_tag.previous_element)
#print(last_a_tag.previous_element.next_element)
#print(last_a_tag.previous_element.next_element.next_element)
#for element in last_a_tag.next_elements:
    #print(repr(element))

#for tag in soup.find_all(re.compile("a")):
    #print(tag.name)
#for ab in soup.find_all(['a','b','p']):
	#print(ab)
#for tag in soup.find_all(True):
    #print(tag.name)
#def has_class_but_no_id(tag):
    #return tag.has_attr('class') and  not tag.has_attr('id')
#for p in soup.find_all(has_class_but_no_id):
	#print(p)

#print(soup.find_all(has_class_but_no_id))

def not_lacie(href):
        return href and not re.compile("lacie").search(href)
a=soup.find_all(href=not_lacie)
print(a)

import re
#def surrounded_by_strings(tag):
    #return (isinstance(tag.next_element, NavigableString)
            #and isinstance(tag.previous_element, NavigableString))

#for tag in soup.find_all(surrounded_by_strings):
    #print(tag.name)
#print(soup.find_all('title'))
#print(soup.find_all("p", "title"))
#print(soup.find_all("a"))
#print(soup.find_all(id="link2"))
#print(soup.find(string=re.compile("sisters")))
#print(soup.find_all(href=re.compile("elsie")))
#print(soup.find_all(id=True))
#print(soup.find_all(href=re.compile("elsie"), id='link1'))
#print(soup.find_all('a','href'))
#data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
#data_soup.find_all(data-foo="value")
#print(data_soup.find_all(attrs={"data-foo": "value"}))
#print(soup.find_all('a',class_='sister'))
#print(soup.find_all(class_=re.compile("itl")))
#def has_six_characters(css_class):
	#return css_class is not None and len(css_class) == 5
#print(soup.find_all(class_=has_six_characters))
#print(soup.find_all(attrs={'class':'sister'}))
#print(soup.find_all(string='Elsie'))
#def is_the_only_string_within_a_tag(s):
	#return(s != s.parent.string)
#print(soup.find_all(string= is_the_only_string_within_a_tag))
#print(soup.title)
#a_string = soup.find(string='Lacie')
#print(a_string)
#first_link = soup.a
#print(first_link)
#print(first_link.find_previous("p"))
#print(soup.select('title'))
tag = soup.b
new_comment = soup.new_string("Nice to see you.", Comment)
tag.append(new_comment)
print(tag,tag.contents)
new_tag = soup.new_tag('a',herf='http://www.example.com')
original_tag = BeautifulSoup("<b></b>").b
original_tag.append(new_tag)
print(original_tag)
new_tag.string = 'Link Text'
print(new_tag)
print(original_tag)

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,'lxml')
tag = soup.a
tag.insert(0,'but did not endorse')
print(tag)

soup = BeautifulSoup("<b>stop</b>")
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_before(tag)
print(soup.b)
soup.b.i.insert_after(soup.new_string('ever'))
print(soup.b)
'''
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup  = BeautifulSoup(markup,'lxml')
print(soup.get_text())