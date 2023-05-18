#!/usr/bin/env python
# coding: utf-8

# What is web scraping?
# 
# when a program or script pretends to be a browser and retrieves web pages, looks at the web pages, extracts info, and then looks at more web pages
# 
# search engines scrape web pages - we call this 'spidering the web' or 'web crawling'

# Why scrape?
# 
# pull data - particularly social data - who links to who?
# 
# get your own data back out of some system that has no 'export capability'
# 
# monitor a site for new info
# 
# spider the web to make a database for a search engine

# https://py4e-data.dr-chuck.net/known_by_Zhen.html

# In[5]:


import re
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = "http://py4e-data.dr-chuck.net/known_by_Zhen.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
n= 0
times  = int(input("Enter count:"))
position = int(input("Enter position:"))

while n < times:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
      count = count + 1
      if count == position: 
         url  = tag.get('href', None)
         print("Retrieving:" , url)
         count = 0
         break
    n = n + 1 


# In[ ]:




