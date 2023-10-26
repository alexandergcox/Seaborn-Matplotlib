#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Creating relational plots with Seaborn 

# This file contains the code snippets that are introduced in the Creating relational plots with Seaborn video. 
# Follow along with the demonstration to:
# - create a relational plot with Seaborn
# - add an additional variable to a relational plot.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import libraries and create a DataFrame

# In[1]:


# Import Matplotlib, Seaborn, and Pandas.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Import the csv file.
penguins = pd.read_csv('penguins.csv')

# View the DataFrame.
print(penguins.shape)
print(penguins.dtypes)
print(penguins.columns)
penguins.head()


# ### 2. Create a relational plot

# In[2]:


# Set the size of the plot.
sns.set(font_scale = 2)

# Create a relational plot.
sns.relplot(x='bill_length_mm', y='flipper_length_mm',
           hue='sex', data=penguins, col='species')


# ### 3. Add another variable

# In[3]:


sns.set(font_scale = 1.5)

sns.relplot(x='bill_length_mm', y='flipper_length_mm',
           hue='sex', data=penguins, col='species',
           row='island')


# In[ ]:




