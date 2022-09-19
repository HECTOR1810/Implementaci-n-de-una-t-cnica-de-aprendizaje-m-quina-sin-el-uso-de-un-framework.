#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./Estatura-peso_HyM.csv')
df = df[["M_estat","M_peso"]]
X_prueba = df[]


# In[ ]:


def beta(x,y):
    t1 = x-average(x)
    t2 = y-average(y)
    Sxy = sum(t1*t2)
    Sxx = sum(t1*)

