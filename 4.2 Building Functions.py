#!/usr/bin/env python
# coding: utf-8

# Can use 'def' to create a function
# 
# Indent the body of the function 
# 
# Defines but does not execute the function!

# In[2]:


x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
x = x+2
print(x)


# In[3]:


#invoking the function
print_lyrics()


# Arguments:
# 
# Arguments are values that we pass into the function as its input
# 
# We use arguments to direct the function to do different things when we callv it at different times
# 
# Put the arguments in paratheses after the name of the function

# In[4]:


big = max('Hello world')
print(big)


# Parameters:
# 
# A variable which we use in the function definition. It is a handle that allows the code in the function to access the arguments

# In[5]:


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


# In[6]:


greet('en')


# In[7]:


greet('fr')


# In[8]:


greet('es')


# Return values:
# 
# Used as the value of the function in the calling expression
# 
# A fruitful function is one that produces a result/return value

# In[9]:


def greet():
    return 'Hello'
    # stops function, determines residual value
print(greet(), 'Glenn')
print(greet(), 'Sally')


# In[10]:


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return'Bonjour'
    else:
        return 'Hello'


# In[11]:


print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')


# Argument goes in () after function
# 
# Parameter is in () inside def of function
# 
# result is the end statement

# Multiple parameters/arguments
# 
# can define more than one parameter in the function def
# 
#     - simply add more arguments 
#     
#     - match the # and order of args and params
#    

# In[12]:


def addtwo(a,b):
    added = a+b
    return added


# In[13]:


x = addtwo(3,5)
print(x)


# In[15]:


def computepay(h, r):
    if h <= 40:
       return h*r
    else:
        return (40*r) + ((h-40)*r*1.5)

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input('Enter rate: ')
r = float(rate)
p = computepay(h, r)
print("Pay", p)


# In[ ]:




