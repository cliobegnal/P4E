#!/usr/bin/env python
# coding: utf-8

# Application Protocol
# 
# TCP gives us a reliable socket
# 
# Appliaction Protocols
# 
#     -Mail
#     
#     -World Wibe Web

# HTTP - Hypertext Transfer Protocol
# 
# the dominant application layer protocol on the internet
# 
# invented for the web - to retrieve HTML, images, docs, etc.
# 
# extended to be data in addition to documents - RSS, web servives, 
# 
# Basic concept - make a conecction - request a document - retrieve the document - close the connection

# HTTP - set of rules to allow browsers to retrieve web documents from servers over the internet

# What is a Protocol?
# 
# a set of rules that all parties follow so we can predict each other's behavior and not bump into each other

# Getting Data from the Server
# 
# each time the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection to the web server and issues a 'GET' request - to GET the content of the page at the specified URL
# 
# the server returns the HTML document to the browser which formats and displays the document to the user

# Internet Standards:
# 
# the standards for all of the internet protocols
# 
# developed by the IETF (Internet Engineering Task Force)
# 
# standards are called 'RFCs' - Request for Comments

# In[1]:


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

