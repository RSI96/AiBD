#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys

df = pd.read_csv('Analized Data.csv', sep=',');
print(df)


# In[2]:


des = df.describe()
print(des)


# In[42]:


df2 = df.query('(TMAX - TMIN) > 238')
print(df2)


# In[41]:


df3 = df.query('TMAX > 251.5 and TMAX < 291.5')
print(df3)


# In[37]:


df4 = df.query('TMIN > 130 and TMIN < 160')
print(df4)


# In[ ]:




