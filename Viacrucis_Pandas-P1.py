#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

cars = pd.read_csv('cars.csv')

head = cars.head()
tail = cars.tail()
headtail = pd.concat([head, tail])

print("The first and last 5 rows of dataframe 'cars':")
headtail

