#!/usr/bin/env python
# coding: utf-8

# Concatenating lists using '+'

# In[1]:


a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)


# Sliced using :

# In[2]:


t = [9,41,12,3,74,15]
t[1:3]


# In[3]:


t[:4]


# Building a list from scratch:
# 
# can create an empty list and add using append()
# 
# the list stays in order and new elements are added at the end

# In[4]:


stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)


# In[5]:


stuff.append('cookie')
print(stuff)


# Is something in a list?
# 
# provides two operators to check: return True or False

# In[6]:


some = [1,9,21,10,16]


# In[7]:


9 in some


# In[8]:


15 in some


# In[9]:


20 not in some


# Lists are in order:
# 
# can hold many items and keeps those items in the order until we change it
# 
# can be sorted with sort()

# In[10]:


friends = ['Joseph','Glenn','Sally']


# In[11]:


friends.sort()
print(friends)


# In[12]:


nums = [3,41,12,9,74,15]
print(len(nums))


# In[13]:


print(max(nums))


# In[14]:


print(min(nums))


# In[15]:


print(sum(nums))


# In[16]:


print(sum(nums)/len(nums))


# In[17]:


numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average: ', average)


# In[ ]:




