#!/usr/bin/env python
# coding: utf-8

# Making 'smart' loops:
# 
# the trick is knowing something about the whole loop when you are stuck writing code that only sees one entry at a time
#    
#    - set some variables to initial values
#            
#            -for thing in data:
#    - look for something or do something to each entry separately, updating a variable
#    
#    - look at the variables

# In[1]:


# Looping through a set
print('Before')
for thing in [9, 41,12, 3, 74, 15]:
    print(thing)
print('After')


# In[3]:


# Finding the largest value
largest = -1
print('Before', largest)
for num in [9,41,12,3,74,15]:
    if num > largest:
        largest = num
        print(largest, num)
print('After', largest)


# In[ ]:




