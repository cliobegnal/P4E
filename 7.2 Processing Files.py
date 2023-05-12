#!/usr/bin/env python
# coding: utf-8

# File Handle as a Sequence
# 
# a file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
# 
# we can use the for statement to iterate through the sequence (ordered set)

# In[ ]:


xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)


# Counting lines in a file:
# 
# open a file read-only
# 
# use a for loop to read each line
# 
# count the lines and print out the number of lines

# In[ ]:


fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)


# In[ ]:


# reading the whold file into a single string
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp)) # 94626
print(inp[:20]) # From stephen.marquar


# In[ ]:


# searching through a file
fhand = open('mbox-short.txt')
for line in fhand:
    if line startswith('From'):
        print(line) #print() adds a new line \n


# In[ ]:


# Can strip off whitespace from the right with rstrip()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line startswith('From'):
        print(line)


# Skipping with Continue
# 
# can conveniently skip a line using continue

# In[ ]:


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line startswith('From'):
        continue #skip the lines we dont want
    print(line) #same as before


# Using 'in' to select lines
# 
# can look for a string anywhere in a line

# In[ ]:


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line) # all lines from that host


# In[ ]:


fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
# 1797 in big mailbox
# 27 in short mailbox


# In[ ]:


# bad file name?
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except: 
    print('File cannot be opened:', fname)
    quit() # i'm quitting, do not continue
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)


# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# In[ ]:


fname = input("Enter file name: ")
fh = open(fname)
print(fh.read().upper().rstrip())


# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# In[ ]:


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
sc = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        sc = (float(sc) + float(line[20:]))
print("Average spam confidence:", sc/count)
# got 0.75 :)

