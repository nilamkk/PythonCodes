#!/usr/bin/env python
# coding: utf-8

# In[141]:


#importing libraries

import pandas as pd


# In[142]:


# reading the files

missing_data=pd.read_csv('missing_emails.csv')
database_data=pd.read_csv('database.csv')


# In[143]:


# showing the data frame

missing_data.head()


# In[144]:


# showing the data frame

database_data.head()


# In[145]:


# setting indices for quick look up 
database_data_with_index=database_data.set_index(['id'])


# In[146]:


# function to fill up nulls

def fillNulls(x):
    if(pd.isnull(x.email)):
        x.email=database_data_with_index.loc[x.id].email #after setting index in database
    return x


# In[147]:


# applying that function to the data frame

missing_data=missing_data.apply(fillNulls,axis=1)


# In[148]:


# saving the output to result.csv

missing_data.to_csv('result.csv',index=False)


# In[ ]:




