#!/usr/bin/env python
# coding: utf-8

# Loops repeat and change each time in a loop

# In[1]:


n = 5
while n > 0:
    print(n)
    n = n-1
print('blast off!')
print(n)


# infinite loops - never end because it stays true forever
# 
# iteration variable is impacted

# zero loop - never runs because it is always false

# Breaking out of a loop - 
# 
# break statement!
# 

# In[2]:


while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


# Finishing an iteration with Continue
# 
# continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

# In[3]:


while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


# In[ ]:




