#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import sys

df = pd.read_csv('Analized Data.csv', sep=',');
print(df)


# In[5]:


des = df.describe()
print(des)


# In[7]:


df2 = df.drop(columns={'id'})
df2=df2.rename(columns={'Unnamed: 0':'model'})
df2 = df2.drop(columns={'model'})
print(df2)


# In[8]:


des = df2.describe()
print(des)


# In[10]:


import matplotlib.pyplot as plt

df2.plot.scatter(x='TMIN',y='TMAX',marker='o')


# In[ ]:




