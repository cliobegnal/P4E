#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type='intl'>
    +1 724 303 4456
    </phone>
    <email hide ='yes'/>
    </person>'''
    
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


# In[2]:


input = '''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute:', item.get('x'))


# In[3]:


import urllib.request, urllib.parse, urllib.error


# In[14]:


address = 'https://py4e-data.dr-chuck.net/comments_1813618.xml'
print("Retrieving " + address)

data = urllib.request.urlopen(address).read()
print("Retrieved: " + str(len(data)) + " characters")

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count:', str(len(counts)))
     
sum = 0
for count in counts:
    sum = sum + int(count.text)
print('Sum:', str(sum))


# In[ ]:




