#!/usr/bin/env python
# coding: utf-8

# In[1]:


x =4
if x > 2:
    print('bigger')
else:
    print('smaller')
print('all done!')


# Multi-way conditionals

# In[2]:


x = 1
if x < 2:
    print('small')
elif x < 10: 
    print('Medium')
else:
    print('LARGE')
print('all done!')


# In[3]:


x = 5
if x < 2:
    print('small')
elif x < 10: 
    print('Medium')
else:
    print('LARGE')
print('all done!')


# In[5]:


x = 50
#block
if x < 2:
    print('small')
elif x < 10: 
    print('Medium')
else:
    print('LARGE')
    
print('all done!')


# If no else - not needed but the code doesn't have to execute
# 
# Can have lots of elif statements
#     
#     -checked in order
# 

# In[6]:


# Which will never print regardless of the value for x?

if x < 2: 
    print('below 2')
elif x>=2:
    print('two or more')
else:
    print('something else')
    # this won't run - no matter what x is, it'll either be less than or equal
    
if x < 2: 
    print('below 2')
elif x < 20:
    print('below 20')
elif x <10:
    print('below 10')
    # this won't run because if it's below 10 it'll already set off x < 20
else:
    print('something else')


# Try and except structure
# 
# surround a dangerous section with try and except
# 
# if it works - except is skipped
# 
# if it fails - it jumps to except section

# In[7]:


astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)


# In[8]:


astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)


# In[9]:


astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)


# In[10]:


rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work!')
else:
    print('Not a number')


# In[ ]:




