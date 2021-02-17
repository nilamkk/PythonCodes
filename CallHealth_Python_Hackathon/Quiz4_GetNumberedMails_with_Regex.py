#!/usr/bin/env python
# coding: utf-8

# In[40]:


#importing libraries

import re 
import pandas as pd

p = re.compile('[0-9]') 


# In[41]:


# reading the files

database=pd.read_csv('database.csv')


# In[42]:


# initial dataframe

database.head()


# In[43]:


# creating the coloumns to add
# assumption: if numbers in the email has more characters in between, it will concate all digits found in the email to op one number

NumericFound=[]
numbers=[]
for i in database.email:
    num="".join(p.findall(i))
    if(num==""):
        NumericFound.append(0)
        numbers.append('NA')
    else:        
        NumericFound.append(1)
        numbers.append(num)


# In[44]:


# adding the columns

database=database.assign(NumericFound=NumericFound,numbers=numbers)


# In[45]:


# after addition

database.head()


# In[46]:


# saving it to result.csv

database.to_csv('result.csv',index=False)


# In[ ]:




