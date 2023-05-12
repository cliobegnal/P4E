#!/usr/bin/env python
# coding: utf-8

# Tuples are like lists:
# 
# indexed starting at 0

# In[2]:


x = ('Glenn', 'Sally','Joseph')
print(x[2])


# In[3]:


y = (1,9,2)
print(y)


# In[4]:


print(max(y))


# In[5]:


for iter in y:
    print(iter)


# Tuples are immutable
# 
# can't alter its contents!

# In[6]:


x = [9,8,7]
x[2] = 6
print(x)


# In[7]:


y = 'ABC'
y[2] = 'D'


# In[8]:


z = (5,4,3)
z[2] = 0


# Can't sort a tuple
# 
# Can't append or extend
# 
# Can't reverse or flip it

# In[9]:


l = list()
dir(1)


# In[10]:


t = tuple()
dir(t)


# Tuples are more efficient
# 
# simpler and more efficient in terms of memory than lists
# 
# tuples > lists for temporary variables

# Tuples and Assignment
# 
# can put a tuple on the left-hand side
# 
# can omit paratheses

# In[11]:


(x,y) = (4, 'fred')
print(y)


# In[12]:


(a,b) = (99,98)
print(a)


# Tuples and Dictionaries
# 
# items() method returns a list of key,value tuples

# In[15]:


d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)


# In[16]:


tups = d.items()
print(tups)


# Tuples are Comparable!
# 
# goes until it can find a difference

# In[17]:


(0,1,2) < (5,1,2)


# In[18]:


(0,1,2000000000) < (0,3,4)


# In[19]:


('Jones','Sally') < ('Jones','Sam')


# Sorting Lists of Tuples
# 
# can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
# 
# using items() and sorted()

# In[20]:


d = {'a':10, 'b':1,'c':22}
d.items()


# In[21]:


sorted(d.items())


# Using sorted()
# 
# can do this even more directly using sorted()

# In[22]:


t = sorted(d.items())
t


# In[23]:


for k,v in sorted(d.items()):
    print(k,v)


# Sort by values instead of keys:
# 
# use a for loop

# In[24]:


c = {'a':10, 'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)


# In[25]:


tmp = sorted(tmp, reverse=True)
print(tmp)


# To find most common words:

# In[26]:


fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = counts.get(word,0) + 1
        
lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)
    
lst = sorted(lst, reverse=True)

for v,k in lst[:10]:
    print(k,v)


# Can do lst = list() through print(k,v) in one line!!
# 
# creates a dynamic list, reverse tuples and then sort

# In[27]:


c = {'a':10, 'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))


# In[36]:


c = {'a':10, 'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()],reverse=True))


# In[37]:


x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)


# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# In[ ]:


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dct = dict()

for line in handle:
    if not line.startswith("From "): 
        continue
    else:
        line = line.split()
        time = line[5]
        hrs = time[:2]
        dct[hrs] = dct.get(hrs,0) + 1
        
for k,v in sorted(dct.items()):
    print(k,v)

