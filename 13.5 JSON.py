#!/usr/bin/env python
# coding: utf-8

# JavaScript Object Notation
# 
# Douglas Crockford
# 
# object literal notation in JS
# 
# represents data as nested lists and dictionaries

# In[5]:


import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes"
        }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])


# In[6]:


input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    } ,
    { "id" : "000",
      "x" : "7",
      "name" : "Chuck"
    }
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('ID', item['id'])
    print('Attribute', item['x'])


# In[ ]:




