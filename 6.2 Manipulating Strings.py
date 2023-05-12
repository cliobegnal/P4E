#!/usr/bin/env python
# coding: utf-8

# String Concatenation with '+'

# In[1]:


a = 'Hello'
b = a + 'There'
print(b)


# In[3]:


c = a + ' ' + 'There'
print(c)


# Using 'in':
# 
# can be used to check if one string is in another
# 
# returns true or false and can be used in an if statement

# In[4]:


fruit = 'banana'
'n' in fruit


# In[5]:


'm' in fruit


# In[6]:


if 'a' in fruit:
    print('Found it!')


# String comparison
# 

# In[8]:


word = 'banana'
if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
if word > 'banana':
    print('Your word, ' + word + ', comes after banana.')  
else:
    print('All right, bananas.')


# String Library
# 
# number of string functions
# 
# do not modify original string, return a new altered string

# In[9]:


greet = 'Hello Bob'
zap = greet.lower()
print(zap)


# In[10]:


print(greet)


# In[11]:


print('Hi There'.upper())


# In[12]:


stuff = 'Hello'
type(stuff)


# In[14]:


# capabilities
dir(stuff)


# In[15]:


word = 'abc'
print(word.capitalize())


# Searching a string:
# 
# use find() to search, finds the first occurence
# 
# if not found, returns -1

# In[16]:


fruit = 'banana'
pos = fruit.find('na')
print(pos)


# In[17]:


aa = fruit.find('z')
print(aa)


# Search and Replace:
# 
# replace() is like search and replace
# 
# replaces all occurences of the search with the replacement

# In[18]:


greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)


# In[19]:


nstr = greet.replace('o', 'x')
print(nstr)


# Stripping Whitespace
# 
# lstrip() and rstrip() remove space
# 
# strip() removes both

# In[20]:


greet = '     Hello Bob  '
greet.lstrip()


# In[21]:


greet.rstrip()


# In[22]:


greet.strip()


# Prefixes

# In[23]:


line = 'Please have a nice day!'
line.startswith('Please')


# In[24]:


line.startswith('p')


# Parsing and Extracting

# In[28]:


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos= data.find('q')
print(atpos)


# In[26]:


sppos = data.find(' ', atpos)
print(sppos)


# In[27]:


host = data[atpos+1:sppos]
print(host)


# In[29]:


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


# In[32]:


x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])


# In[ ]:




