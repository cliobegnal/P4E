#!/usr/bin/env python
# coding: utf-8

# Regular Expressions - 
# 
# provides a concise and flexible means for matching strings of text, such as particular characters, words, or patterns of characters
# 
# written in a formal language that can be interpreted by a regex processor

# Understanding RegEx:
# 
# powerful and cryptic
# 
# fun once you understand
# 
# language unto themselves
# 
# language of marker characters

# ^ matches the beginning of a line
# 
# $ matches the end
# 
# . matches any character
# 
# \s matches whitespace
# 
# \S matches non-whitespace
# 
# '*' repeats a character 0 or more times
# 
# *? repeats a character 0 or more times (non-greedy)
# 
# '+' repeats a character 1 or more times
# 
# +? repeats a chracter 1 or more times (non-greedy)
# 
# [aeiou] matches a single chracter in the listed set
# 
# [^XYZ] matches a single character not in the listed set
# 
# [a-z0-9] set of characters can include a range
# 
# ( indicates where string extraction starts
# 
# ) indicates where string extraction ends

# RegEx Module:
# 
# must import with 'import re'
# 
# can use re.search() to see if a string matches
# 
# can use re.findall() to extract portions of a string that match

# In[1]:


import re


# In[ ]:


# like find()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


# In[ ]:


# line startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)


# Wild card characters:
# 
# dot character matches any character
# 
# if you add the asterisk, the character is 'any number of times'

# In[ ]:


^X.*:
# looks for lines that have an X at the beginning followed by any number of characters, followed by a colon


# In[ ]:


# can clean (dont want spaces?)
^X-\S+:
# matches that start with X- followed by non-whitespace + one or more times

