#!/usr/bin/env python
# coding: utf-8

# Algorithms: a set of rules or steps used to solve a problem
# 
# Data Structures: a particular way of organizing data in a computer

# A list is a kind of collection:
# 
#     -allows us to put many values in a single variable
#     
#     -carries many values in one package
# 

# In[1]:


friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks','shirt','perfume']


# List Constants:
# 
# surrounded by [] and the elements are separated by commas
# 
# can be any Python object, even another list
# 
# can be empty

# In[2]:


print(friends)


# In[3]:


print([])


# In[4]:


print(['red',1,[5,6]])


# In[5]:


for friend in friends:
    print('Hi', friend)


# In[6]:


print(friends[1])


# Lists are mutable!
# 
# Strings are immutable and cant be changed
# 
# Lists are mutable and can be changed using indexing

# In[7]:


fruit = 'Banana'
fruit[0] = 'b'


# In[8]:


lotto = [2,14,26,41,63]
print(lotto)


# In[9]:


lotto[2] = 28
print(lotto)


# How long is a list?
# 
# len() takes a list and returns the number of elements

# In[10]:


greet = 'Hello Bob'
print(len(greet))


# In[11]:


x = [1,2,'joe',99]
print(len(x))


# Using the range function
# 
# returns a list of numbers that range from zero to one less than the parameter

# In[12]:


print(range(4))


# In[13]:


print(range(len(friends)))


# In[15]:


for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)


# In[ ]:




