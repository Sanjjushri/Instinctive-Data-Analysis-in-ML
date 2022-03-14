#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from lazypredict.Supervised import LazyClassifier


# In[25]:


df = pd.read_csv("../datasets/Iris.csv")


# In[26]:


missing = df.isnull().values.any()


# In[27]:


if missing == True:
    df = df.ffill().bfill()
    print("null values filled")
else:
     print("no null values encountered")


# In[28]:


label = preprocessing.LabelEncoder() 


# In[29]:


object_col = df.select_dtypes(include=['object']).columns


# In[30]:


for name in object_col:
    df[name] = label.fit_transform(df[name]) 


# In[31]:


df.drop_duplicates(inplace=True)


# In[32]:


X = df.iloc[:,:-1]
Y = df[df.columns[-1]]


# In[33]:


X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=.3,random_state =23)
classi=LazyClassifier(verbose=0,predictions=True)


# In[34]:


models_c,predictions_c=classi.fit(X_train, X_test, Y_train, Y_test)


# In[35]:


models_c


# In[ ]:




