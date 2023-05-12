#!/usr/bin/env python
# coding: utf-8

# Counting Pattern:
# 
# count the words in a line of text by split() and then loop through the words, using a dict to track each count

# In[1]:


counts = dict()
print('Enter a line of text: ')
line = input(' ')
words = line.split()
print('Words:', words)
print('Counting ... ')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)
# the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car


# Definite Loops and Dictionaries
# 
# can write a for loop that goes through all entries - actually goes through all keys and looks up the values

# In[2]:


counts = {'chuck':1,'fred':42,'jan':100}
for key in counts:
    print(key,counts[key])


# Retrieving lists of keys and values

# In[3]:


jjj = {'chuck':1,'fred':42,'jan':100}
print(list(jjj))


# In[4]:


print(jjj.keys())


# In[5]:


print(jjj.values())


# In[6]:


print(jjj.items())


# Bonus: Two Iteration Variables
# 
# loop through key-vaklue pairs in a dict using two iteration variables
# 
# the first is the key and the second is the value

# In[7]:


for aaa,bbb in jjj.items():
    print(aaa,bbb)


# In[ ]:


name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    # dont need to do strip bc split does it for you
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)


# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# In[9]:


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()

for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)


# In[ ]:




