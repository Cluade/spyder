from bs4 import BeautifulSoup as bs
import bs4
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""  

soup = bs(html)  
"""
#print(soup.prettify())
print(soup.a)
#print(soup.p.attrs)

#print(soup.p.string)

if type(soup.a.string)==bs4.element.Comment:
    print(soup.a.string)

for child in soup.body.children:
    print(child)

for child in soup.descendants:
    print(child)
"""
"""
for string in soup.strings:
    print(repr(string))

p = soup.a
print(p.parent)

content = soup.head.title.string
for parent in  content.parents:
    print(parent.name)
"""

#print(soup.p.next_element)

#for sibling in soup.a.previous_siblings:
#    print(repr(sibling))

#print(soup.find_all('a'))

#for tag in soup.find_all(re.compile("^h")):
    #print(tag.name)
"""
for tag in soup.find_all(["a", re.compile("^h")]):
    print(tag.href)

for tag in soup.find_all(True):
    print(tag.name)

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')  

print(soup.find_all(has_class_but_no_id))

print(soup.find_all(href=re.compile("ie"),id='link1'))

data_soup = bs('<div data-foo="value">foo!</div>')
print(data_soup.find_all(attrs={"data-foo": "value"}))
print(soup.find_all(text=re.compile("Dormouse")))
for index, cot in enumerate(soup.find_all(text=re.compile("Dormouse"))):
    print(index,cot)
"""
#print(soup.select('.sister'))
#print(soup.select('p #link1'))
print(soup.select('p a[href="http://example.com/elsie"]'))