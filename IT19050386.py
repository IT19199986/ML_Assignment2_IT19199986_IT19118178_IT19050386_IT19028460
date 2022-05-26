#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#making statistical graphics
import seaborn as sns

#after execute code immediatly execute charts
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#import data set
data = pd.read_csv('heart.csv')


# In[3]:


data


# In[4]:


#returns the first n rows for the object based on position.
data.head()


# In[5]:


#Data Analysis


# In[6]:


#information about the data set
data.info()


# In[7]:


print('The shape of our features is:', data.shape)


# In[ ]:




