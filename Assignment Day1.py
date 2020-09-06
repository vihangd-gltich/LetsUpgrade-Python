#!/usr/bin/env python
# coding: utf-8

# # Day 1 Assignment

# In[1]:


lst=['Vd',1,2,3.5,['no','2']]


# In[2]:


lst


# In[3]:


lst.append('Python')


# In[4]:


lst


# In[7]:


lst.index(2)


# In[11]:


lst.count('Python')


# In[10]:


lst.count(1)


# In[12]:


lst.remove('Python')


# In[13]:


lst


# In[14]:


lst.pop(-2)


# In[15]:


lst


# In[16]:


dit={"name":"vihang","age":"22","city":"pune","email":"dusanevihang2@gmail.com"}


# In[17]:


dit


# In[18]:


dit.items()


# In[19]:


dit.keys()


# In[20]:


dit.values()


# In[21]:


dit.pop('age')


# In[22]:


dit


# In[28]:


dit.clear()


# In[29]:


dit


# In[30]:


dit["school"]="SYmbi"


# In[31]:


dit


# In[32]:


st={"vihang","dusane",1,2,3,4,5,5}


# In[33]:


st


# In[34]:


st1={"vihang",2,6,8}


# In[35]:


st1


# In[36]:


st.union(st1)


# In[37]:


st.issubset(st1)


# In[38]:


st.difference(st1)


# In[39]:


st.intersection(st1)


# In[40]:


st.symmetric_difference(st1)


# In[45]:


st1.pop()


# In[46]:


st


# In[47]:


st1


# In[48]:


tup=("vid","Maharashtra","India","MAle")


# In[49]:


tup


# In[50]:


tup.count("India")


# In[52]:


tup.index("MAle")


# In[53]:


str="letsUpgrade"


# In[54]:


str


# In[57]:


str.capitalize()


# In[58]:


str.find('u')


# In[59]:


str.casefold()


# In[60]:


str.isdecimal()


# In[61]:


str.endswith('e')


# In[64]:


str.strip()


# In[ ]:




