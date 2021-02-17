#!/usr/bin/env python
# coding: utf-8

# # Second here 

# In[112]:


#importing libraries

import pandas as pd


# In[113]:


# reading the files

student_scores=pd.read_csv('student_scores.csv')


# In[114]:


# showing the data frame

student_scores.head()


# In[115]:


# function to create tags 

def fillTag(x):
    newTag=[]
    for i in x.marks:
        if(i>85):
            newTag.append('merit')
        elif (i>78):
            newTag.append('passed')
        else:
            newTag.append('failed')
    return newTag


# In[116]:


# creating tags

student_scores=student_scores.assign(tag=fillTag)


# In[117]:


# after creating tags

student_scores.head()


# In[118]:


# saving it as result.csv

student_scores.to_csv('result.csv',index=False)

