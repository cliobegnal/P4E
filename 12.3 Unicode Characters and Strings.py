#!/usr/bin/env python
# coding: utf-8

# ASCII - American Standard Code for Information Exchange:
# 
# This number = certain letter

# Representing Simple Strings:
# 
# each character represented by 0 through 256 and stored in 8 bits of memory
# 
# 8 bits = 1 byte
# 
# ord() tells us the numeric value

# In[1]:


print(ord('H'))


# In[2]:


print(ord('e'))


# In[3]:


print(ord('\n'))


# Unicode - Universal Code for characters

# Multi-Byte Characters:
# 
# to represent the wide range of characters, computers must handle characters with more than one byte
# 
# UTF-16 : fixed length, two bytes
# 
# UTF-32 : fixed length, four bytes
# 
# UTF-8 : one to four bytes
# 
#     -upwards compatible with ASCII
#     
#     -automatic detection between ASCII and UTF-8
#     
#     -UTF-8 is recommended practice for encoding data to be exchanged between systems

# Would prefix u before a quote for unicode, now they're both strings

# Python 3 and Unicode:
# 
# all strings are unicode
# 
# working with str variables usually jut works
# 
# have to encode and decode data using sockets (UTF-8)

# Python strings to bytes:

# In[ ]:


while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ):
        break
    mystring = data.decode()
    # bytes to unicode
    print(mystring)


# An HTTP request:

# In[ ]:


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.o\n\n'.encode() #unicode to bytes


# In[ ]:




