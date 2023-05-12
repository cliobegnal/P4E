#!/usr/bin/env python
# coding: utf-8

# Second kind of collection: (lists and dictionaries)
# 
# more than one value added to a single variable

# Dictionaries:
#     
# most powerful data collection
# 
# fast database-like operations
# 
# different names in dfferent languages:
#     
#     -associative arrays (perl/php)
#     
#     -properties or map or hashmap (java)
#     
#     -property bag (c#/.net)
# 
# list index their entries but dictionaries have no order
# 
# index with a lookup tag

# In[3]:


purse = dict()
# key          # value
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)


# In[2]:


purse['candy'] = purse['candy'] + 2
print(purse)


# Dictionaries are like lists but use keys instead of numbers to look up values

# In[4]:


ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)


# Dictionary literals:
# 
# use curly braces and have a list of key:value pairs
# 
# can make an empty dictionary with {}

# In[5]:


jjj = {'chuck':1,'fred':42,'jan':100}
print(jjj)


# In[6]:


ooo = {}
print(ooo)


# In[ ]:




