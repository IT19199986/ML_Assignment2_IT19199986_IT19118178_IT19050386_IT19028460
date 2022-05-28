#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import all the libraries 

#used for complex mathematical operations
import numpy as np

#used for data analysis
import pandas as pd

#used for data visualization and graphical plotting
import matplotlib.pyplot as plt

#making statistical graphics
import seaborn as sns

#after execute code immediatly execute charts
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#import the data set
#used pandas library
data = pd.read_csv('heart.csv')


# In[3]:


#data set preview
data


# In[4]:


#returns the first n rows of the dataset with column name
data.head()


# In[ ]:





# In[5]:


#Data Analysis


# In[6]:


#information about the data set
data.info()


# In[7]:


#size of the datset
print('The shape of our features is:', data.shape)


# In[ ]:




