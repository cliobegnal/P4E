#!/usr/bin/env python
# coding: utf-8

# Using urllib:

# In[1]:


import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


# Like a file ...

# In[2]:


counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


# In[4]:


fhand2 = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand2:
    print(line.decode().strip())


# The easy way - Beautiful Soup
# 
# can do string searches the hard way

# In[5]:


from bs4 import BeautifulSoup


# In[6]:


url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all anchor tags
tags = soup('a')
# list of anchor tags
for tag in tags:
    print(tag.get('href', None))
# href = ' ' text


# Chapter Summary:
# 
# TCP/IP gives us pipes/sockets between applications
# 
# we designed application protocols to make use of those pipes
# 
# HTTP is a simple yet powerful protocol
# 
# python has good support for sockets, HTTP, and HTML parsing

# Sample Code:

# In[9]:


# ignore SSL certificate errors
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
# list of anchor tags
for tag in tags:
    print(tag.get('href', None))


# In[17]:


import re 

html = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1813616.html').read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0

for tag in tags:
    x = str(tag)
    y = re.findall("[0-9]+", x)
    for num in y:
        num = int(num)
        sum = sum + num
print(sum)
    


# In[ ]:




