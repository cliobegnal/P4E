#!/usr/bin/env python
# coding: utf-8

# Constants = fixed values such as numbers, letters, and strings

# In[1]:


print(123)


# In[2]:


print(98.6)


# In[3]:


print('Hello world')


# reserved words:
# 
# False   None   True   and   as   assert   break   class   if   def   del   elif
# else   except   return   for   from   global   try   import   in   is   lambda
# while   not   or   pass   raise   finally   continue   nonlocal   with   yield
# 

# variable = named place in the memory where a programmer can store data and later retrieve using the variable name

# In[4]:


x = 12.2
y = 14
x = 100 # changes x from 12.2 to 100


# naming rules - must start with a letter or underscore, must consist of letters/numbers/underscores, case sensitive
# 
# good - spam   eggs   spam 23 _speed
# 
# bad - 23 spam   #sign var.12
# 
# different - spam Spam SPAM

# In[6]:


x1q3z9ocd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ocd * x1q3z9afd
print(x1q3p9afd)
# multiplies the two badly named variables
    # fine for python but not us
        # a = 35.0
        # b = 12.50
        # c = a*b
        # print(c)


# Assignment statements = assigning a value to a variable with '='

# In[9]:


x = .6
x = 3.9 * x * (1-x)
print(x)

