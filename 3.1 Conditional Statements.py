#!/usr/bin/env python
# coding: utf-8

# 'if' statements!
# 
# condition like a question
# 
# may or may not run!

# In[1]:


x = 5
if x < 10: 
    #indent after colon
    print('smaller')
if x > 20:
    print('bigger')
print('finish!')


# Comparison operators:
# 
# < is less than
# 
# <= is less than or equal to
# 
# == is equal to
# 
# '>=' is greater than or equal to
# 
# '>' is greater than
# 
# != is not equal
# 
# Booleans - true or false / yes or no
# 
# = is only used to assignment

# In[2]:


x = 5
if x ==5:
    print('equals 5')
if x > 4:
    print('greater than 4')
if x>=5:
    print('greater than or equal to 5')
if x < 6:
    print('less than 6')
if x <=5:
    print('less than or equal to 5')
if x !=6:
    print('not equal to 6')


# In[3]:


x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')


# In[7]:


# indented to show which block it's a part of
x = 5
if x > 2:
    print('bigger than 2')
    print('still bigger than 2')
print('dont with 2')
for i in range(5):
    print(i)
    if x > 2:
        print('bigger than 2')
        #block within a block!
    print('done with i:', i)
print('all done!')
    


# In[8]:


# nested decisions
x = 42
if x >1:
    print('more than 1')
    if x < 100:
        print('less than 100')
print('all done!')


# Two way decisions:
# 
# Do one thing if something is true and another if it's false
# 
# like a fork in the road

# In[9]:


x =4
if x > 2:
    print('bigger')
else:
    print('not bigger')
print('all done!')


# In[ ]:




