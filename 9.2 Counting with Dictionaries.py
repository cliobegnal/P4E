#!/usr/bin/env python
# coding: utf-8

# Many counters with dictionaries:
# 
# counting to see how often we see something

# In[5]:


ccc = dict()
ccc['csev'] = 1 
ccc['cwen'] = 1
print(ccc)


# In[6]:


ccc['cwen'] = ccc['cwen'] + 1
print(ccc)


# Dictionary tracebacks
# 
# an error to reference a key that isnt in the dict
# 
# can use 'in' to see!

# In[7]:


print(ccc['csev'])


# In[8]:


print(ccc['zhen'])


# In[10]:


'zhen' in ccc


# When we see a new name:
# 
# need to add a new entry in the dict

# In[11]:


counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


# The 'get' method for dictionaries:

# In[14]:


if name in counts:
    x = counts[name]
else:
    x=0
x = counts.get(name,0)
print(x)


# Simplified counting with get()
# 
# can use get() and provide a default value of zero when they key is not yet in the dictionary - and then just add one

# In[15]:


counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)


# In[ ]:




