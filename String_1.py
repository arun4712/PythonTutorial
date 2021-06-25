#!/usr/bin/env python
# coding: utf-8

# #Strings-Single Line String and Multi Line String

# In[8]:


s='how are you'
print(s)


# In[10]:


s="how are you"
print(s)


# In[11]:


s='''how are you?
    i am fine.
    glad to know this.'''
print(s)                 


# In[12]:


s="""how are you?
    i am fine.
    glad to know this."""
print(s)   


# In[14]:


s="""my name is {}.I am software {}"""


# In[15]:


s.format("arun","professional")


# In[19]:


s="""my name is {1}.I am software {0}"""


# In[20]:


s.format("arun","professional")


# In[21]:


s = "How are you!"
print(s)


# In[24]:


s = "How\nare\n\t\tyou!"
print(s)


# ###Python String | ljust(), rjust(), center(),zfill()

# In[69]:


s = "50"
s1 = s.ljust(20)
s2 = s.rjust(20)
s3 = s.center(20)
s4 = s.zfill(20)


# In[70]:


print(repr(s))
print(repr(s1))
print(repr(s2))
print(repr(s3))
print(repr(s4))


# In[63]:


txt = "50"
x = txt.zfill(10)

print(x)


# In[26]:


s = "How are you my friend"
s1 = s.center(30, '=')
print(s1)


# In[ ]:




