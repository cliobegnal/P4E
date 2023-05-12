#!/usr/bin/env python
# coding: utf-8

# Numeric expressions:
# 
# '+' Addition
# 
# '-' Subtraction
# 
# '*' Multiplication
# 
# / Division
# 
# ** Power
# 
# % Remainder
# 

# In[1]:


xx = 2
xx = xx + 2
print(xx)


# In[3]:


yy = 440 * 12
print(yy)


# In[5]:


zz = yy / 1000
print(zz)


# In[6]:


jj = 23
kk = jj % 5
print(kk)


# In[7]:


print(4**3)


# Order of Evaluation
# 
# to show precedence - add parathesis

# In[9]:


x = 1 + (2 * 3) -(4 / (5 **  6))
print(x)


# PEMDAS for order without added parenthesis

# In[11]:


x = 1 + 2 ** 3 / 4 * 5
print(x)


# Type - difference between variables, literals, and constants
# 
# '+' is addition or concatenate

# In[12]:


ddd = 1 + 4 
print(ddd)


# In[14]:


eee = 'hello ' + 'there'
print(eee)


# Can't add 1 to a string !

# In[15]:


eee = eee + 1


# Traceback error stops the script!

# In[19]:


type(eee)
#sees the type of the variable


# Integers - whole numbers
# 
# Floats - decimal points

# In[21]:


xx = 1
type(xx)


# In[20]:


temp = 98.6
type(temp)


# When you put an integer and float into an expression, the int is automatically converted to a float
# 
# can be controlled with int() or float()

# In[22]:


print (float(99)+100)


# In[23]:


i = 42
type(i)


# In[24]:


f = float(i)
print(f)


# In[25]:


type(f)


# Integer division produces a float result!

# In[26]:


print(10/2)


# In[27]:


print(99.0/100.0)


# In[28]:


print(9/2)


# Can also use int() and float() to convert between strings and integers

# In[30]:


sval = '123'
type(sval)


# In[31]:


print(sval +1)


# In[33]:


ival = int(sval)
type(ival)


# In[34]:


print(ival +1)


# In[35]:


nsv = 'hello'
niv = int(nsv)


# User input - input()
# 
# Returns as a string!

# In[38]:


name = input('Who are you? ')
print('Welcome ' + name + '!')

