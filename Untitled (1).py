#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../../datasets/IMDB_review/IMDB Dataset.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[11]:


import re
def clean_html(review):
    return re.sub('<.*?>', ' ',review)


# In[12]:


reviews = df['review'].apply(clean_html)


# In[13]:


reviews


# In[17]:


reviews.iloc[0]


# In[ ]:




