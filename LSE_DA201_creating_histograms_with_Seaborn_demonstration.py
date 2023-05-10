#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Creating histograms with Seaborn (tutorial video)

# This file contains the code snippets that are introduced in the Creating histograms with Seaborn video. 
# Follow along with the demonstration to:
# - create a histogram
# - change histogram bin size.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import libraries and create a DataFrame

# In[1]:


# Import Matplotlib, Seaborn, and Pandas.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Import the csv file.
fitness = pd.read_csv('daily_activity.csv')

# View the DataFrame.
print(fitness.shape)
print(fitness.dtypes)
print(fitness.columns)
fitness.head()


# ### 2. Create a histogram

# In[2]:


# Create a single_day variable.
# Specify a chosen day within the ActivityDate column and fitness DataFrame.
single_day = fitness[fitness['ActivityDate'] == '4/12/2016']

# View the output.
print(single_day.shape)

# Create a histogram with the histplot() function.
sns.histplot(data=single_day, x='TotalDistance')


# ### 3. Change the bin size

# In[3]:


# Change the bin size to 1.
# Create the histogram and set binwidth=1.
sns.histplot(data=single_day, x='TotalDistance', binwidth=1)


# In[4]:


# Change the bin size to 2.
# Create the histogram and set binwidth=2.
sns.histplot(data=single_day, x='TotalDistance', binwidth=2)


# In[ ]:




