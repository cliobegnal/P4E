#!/usr/bin/env python
# coding: utf-8

# Split() breaks a string into parts and produces a list of strings

# In[1]:


abc = 'With three words'
stuff = abc.split()
print(stuff)


# In[2]:


print(len(stuff))


# In[3]:


print(stuff[0])


# In[4]:


for w in stuff:
    print(w)


# When you don't specify a delimiter, multiple spaces are treated like one
# 
# Can specify what delimiter to use in splitting

# In[5]:


line = 'A lot                of spaces'
etc = line.split()
print(etc)


# In[6]:


line = 'first;second;third'
thing = line.split()
print(thing)


# In[7]:


print(len(thing))


# In[8]:


thing = line.split(';')
print(thing)


# In[9]:


print(len(thing))


# In[10]:


line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)


# Double Split Pattern
# 
# can split a line and then grab one of the pieces and split it again

# In[12]:


email = words[1]
print(email)


# In[13]:


pieces = email.split('@')
print(pieces)


# In[14]:


pieces[1]


# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

# In[ ]:


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    now = line.rstrip().split()
    for word in now:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)


# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.

# In[ ]:


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    now = line.rstrip().split()
    if 'From' in now:
        print(now[1])
        count = count + 1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")

