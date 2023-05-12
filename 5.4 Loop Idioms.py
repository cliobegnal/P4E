#!/usr/bin/env python
# coding: utf-8

# Counting in a Loop:
# 
# introduce a counter variable that starts at 0 and add one for each loop

# In[5]:


zork = 0
print('Before', zork)
for num in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, num)
print('After', zork)


# Summing in a Loop:
# 
# introduce a sum variable starting at 0 and adding the value each time

# In[6]:


zork = 0
print('Before', zork)
for num in [9,41,12,3,74,15]:
    zork = zork+num
    print(zork, num)
print('After', zork)


# Finding the Average:
# 
# combines the counting and sum and divides when the loop is done

# In[7]:


count = 0
sum = 0
print('Before', count, sum)
for num in [9,41,12,3,74,15]:
    count = count+1
    sum = sum + num
    print(count, sum, num)
print('After', count, sum, sum/count)


# Filtering in a Loop:
# 
# if statement to catch/filter the values we want

# In[10]:


print('Before')
for num in [9,41,12,3,74,15]:
    if num > 20:
        print('Large number', num)
print('After')


# Search Using a Boolean:
# 
# Start at False and set to True when we find what we're looking for

# In[11]:


found = False
print('Before', found)
for num in [9,41,12,3,74,15]:
    if num == 3:
        found = True
    print(found, num)
print('After', found)


# Smallest value

# In[12]:


smallest = 100
print('Before', smallest)
for num in [9,41,12,3,74,15]:
    if num < smallest:
        smallest = num
    print(smallest, num)
print('After', smallest)


# In[14]:


smallest = None
print('Before')
for num in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print(smallest, num)
print('After', smallest)


# 'is' and 'is not' Operators:
# 
# Used in logical expressions
# 
# Implies "is the same as"
# 
# Similar to but stronger than ==
# 
# is not also is a logical operator

# In[16]:


largest = None
smallest = None
while True:
    try:
        n = input("Enter a number: ")
        if n == "done":
            break
        n = int(n)
        if largest is None:
            largest = n
            continue
        if n > largest:
            largest = n
            continue
        if smallest is None:
            smallest = n
            continue
        if n < smallest:
            smallest = n
            continue
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)


# In[ ]:




