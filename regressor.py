#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from lazypredict.Supervised import LazyRegressor


# In[3]:


df = pd.read_csv("../datasets/vegetable_price.csv")


# In[4]:


missing = df.isnull().values.any() 


# In[5]:


if missing == True:
    df = df.ffill().bfill()
    print("null values filled")
else:
     print("no null values encountered")


# In[6]:


label = preprocessing.LabelEncoder() 


# In[7]:


object_col = df.select_dtypes(include=['object']).columns


# In[8]:


for name in object_col:
    df[name] = label.fit_transform(df[name]) 


# In[11]:


X = df.iloc[:,:-1]
y = df[df.columns[-1]]


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.3,random_state =123)


# In[13]:


reg = LazyRegressor(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = reg.fit(X_train, X_test, y_train, y_test)


# In[14]:


models


# In[ ]:




