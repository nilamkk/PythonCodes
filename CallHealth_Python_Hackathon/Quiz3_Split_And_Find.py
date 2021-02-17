#!/usr/bin/env python
# coding: utf-8

# In[68]:


#importing libraries

import pandas as pd


# In[69]:


# reading the files

database=pd.read_csv('database.csv')


# In[70]:


# creating dict for quick look up

dict={}

for i in database.email:
    word=i.split('@')
    dict[word[0]]=(word[1])


# In[71]:


# reading users from users10.txt

fileRead=open('users10.txt',"r")


users= [i.strip() for i in fileRead.readlines()]

for i in users:
    print(i,end=" ")

fileRead.close()


# In[72]:


# creating the list to be written in the output file

listFinal=[]

for i in users:
    try:
        listFinal.append({i:"".join([i,'@',dict[i]])})
    except KeyError:
        print(i, ' not found')


# In[73]:


# list to write

listFinal


# In[74]:


# writing the list to result.txt

file1=open("result.txt","w")

l=str(listFinal)

file1.write(l)

file1.close()

