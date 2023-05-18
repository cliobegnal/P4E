#!/usr/bin/env python
# coding: utf-8

# Transport Control Protocol (TCP):
# 
# built on top of IP (internet protocol)
# 
# assumes IP might lose some data - stores and retransmits data if it seems to be lost
# 
# handles 'flow control' using a transmit window
# 
# provides a nice reliable pipe

# TCP Connections / Sockets:
# 
# an Internet socket is an endpoint of a bideirectional inter-process communication flow across an IP-based computer network, such as the Internet

# TCP Port Numbers:
# 
# a port is an application-specific or process-specific software communications endpoint
# 
# allows multiple networked applications to coexist on the same server
# 
# list of well-known TCP port numbers
#     
#     -port 80 (web server)
#     
#     -port 443 (https://)
#     
#     -telnet (23) 
# 

# Sockets in Python:
# 
# built in support

# In[2]:


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )

