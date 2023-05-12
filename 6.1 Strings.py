#!/usr/bin/env python
# coding: utf-8

# String data type:
# 
# a sequence of characters
# 
# uses quotes '' or ""
# 
# '+' means concatenate
# 
# can convert numbers in a string into a number with int()
# 

# In[1]:


print('Hello world!')


# Reading and Converting:
# 
# read data in with strings and then parse and convert as needed
# 
# using input() function!
# 
# input() numbers need to be converted from strings

# In[3]:


name = input('Enter name: ')
print('Hello', name)


# Looking inside strings:
# 
# Can index a single character with []
#     
#     -Starts at 0!!!
# 

# In[4]:


fruit = 'banana'
letter = fruit[1]
print(letter)


# In[5]:


x = 3
w = fruit[x-1]
print(w)


# Will get an error if you attempt to index beyond the end of a string!

# In[6]:


zot = 'abc'
print(zot[5])


# Strings have length
# 
#     -len() gives us the length
# 
#     -is another built-in function that takes an input and produces an output

# In[7]:


fruit = 'banana'
print(len(fruit))


# Looping through strings
# 
# Using a while statement and an iteration variable and the len function, we can construct a loop to look at each letter individually

# In[8]:


fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


# Using a for statement is better!

# In[9]:


fruit = 'banana'
for letter in fruit:
    print(letter)


# Looping and Counting:
#     
#     -can count the number of letters in a string

# In[10]:


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# Looking deeper into 'in':
# 
# the iteration variable iterates through the sequence!

# Slicing strings:
# 
# can look at any section of a string with a colon
# 
# the second number is one beyond the end
#     
#     -up to but not including
# 
# if second number is beyond the end, it stops at the end

# In[11]:


s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])


# Leaving off the first number goes from the beginning
# 
# Leaving off the last goes to the end

# In[12]:


s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])


# In[ ]:




