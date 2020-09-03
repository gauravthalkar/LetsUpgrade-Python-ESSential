#!/usr/bin/env python
# coding: utf-8

# #                               # ASSIGNMENT-1 | DAY 2

# # List and its functions

# In[ ]:


lst = [1,2,3,6.6,7.7,8.8,"ABC","XYZ","PQR",[1,2]]
lst


# In[13]:


lst.append(5)
lst


# In[3]:


lst.pop(3)


# In[4]:


lst.index(2)


# In[8]:


lst.copy()


# In[14]:


lst.reverse()
lst


# In[19]:


lst.clear()
lst


# # Dictionaries AND its functions

# In[21]:


dit = {"firstname":"robert","lastname=":"jr","age":"50","place":"florida","mobno":"8080313233"}
dit


# In[22]:


dit.get("age")


# In[24]:


dit.pop("firstname")


# In[25]:


dit.keys()


# In[26]:


dit.items()


# In[27]:


dit.values()


# In[30]:


dit.clear()
dit


# # Sets And Its Functions
# 

# In[1]:


st = {"ABC","PQR",1,2,3,4,5,5,6,6,6}
st


# In[3]:


st.add(7)
st


# In[9]:


st.discard(3)
st


# In[11]:


st.pop()


# In[12]:


st.union()


# In[16]:


st1 = {5,6,7}
st1.intersection(st)


# In[17]:


st1.issubset(st)


# # Tuples AND Its Functions
# 

# In[19]:


tup = ("ABC","@","PQR.XYZ","LMN")
tup


# In[20]:


tup.count("@")


# In[21]:


tup.index("LMN")


# In[23]:


len(tup)


# In[25]:


any(tup)


# In[26]:


enumerate(tup)


# # String And Its Functions

# In[56]:


str = "assignment DAY Two"
str


# In[57]:


str.upper()


# In[58]:


str.replace("Two","Three")  


# In[60]:


str.capitalize()


# In[61]:


str.lower()


# In[63]:


str.find("DAY")

