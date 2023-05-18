#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# Matching and Extracting Data:
# 
# re.search() returns a T/F depending on whether the string matches
# 
# If we want all matching strings to be extracted, use re.findall()

# In[2]:


x = 'My favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # one or more digits
print(y)


# When we use re.findall(), it returns a list of zero or more substrings that match

# In[3]:


y = re.findall('[AEIOU+]',x)
print(y)


# The repeat characters (* and +) push outward in both directions to match the largest possible string

# In[5]:


x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)


# In[6]:


# Add ? to not be greedy
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)


# Fine-tuning string extraction:

# In[7]:


x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y)


# In[9]:


# () say where to start and stop!
y = re.findall('(\S+@\S+)',x)
print(y)


# In[10]:


atpos = x.find('@')
print(atpos)


# In[11]:


sppos = x.find(' ',atpos)
print(sppos)


# In[12]:


host = x[atpos+1 : sppos]
print(host)


# Double Split Pattern:
# 
# split a line one way, then grab one of the pieces and split it again

# In[17]:


line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


# In[18]:


y = re.findall('@([^ ]*)',line)
print(y)


# In[21]:


y = re.findall('^From.*@([^ ]*)',line)
print(y)


# In[ ]:


numlist = list()
for line in hand:
    line = linestrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist)) # Max = 0.8475


# Escape Character: '\'

# In[23]:


x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)


# Cheat Sheet:
# 
# https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt

# In[24]:


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)


# In[29]:


line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@\S+',line)
print(y)


# In[58]:


import re
handle = open('regex_sum.txt')
numlist = 0
for line in handle:
    line = line.rstrip()
    numlist = numlist + sum(map(lambda x: int(x), re.findall('([0-9]+)', line)))

print(numlist)


# In[ ]:




