#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Create line and subplots

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app that provides recommendations based on the last movie you watched. As a part of their process, they want to review the data and gather enough information before they start making suggestions and recommendations to their clients. 
# 
# This analysis uses the `movies.csv` and `ott.xlsx` data sets. Based on the available information, in this activity you will:
# - create a line chart to help identify trends in the data and spot or track interesting relationships among the variables
# - understand what the data says by visualising it with lineplots.

# ## 1. Import the libraries

# In[1]:


# Import necessary libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ## 2. Import Excel file

# In[2]:


# Load the Excel data using pd.read_excel.
ott = pd.read_excel('ott.xlsx')

# View the columns.
print(ott.columns)


# ## 3. Import CSV file

# In[3]:


# Load the CSV data using pd.read_csv.
movies = pd.read_csv('movies.csv')

print(movies.columns)


# ## 4. Validate the DataFrames

# In[4]:


# Data imported correctly?
print(movies.head())
print(movies.shape)
print(movies.dtypes)


# In[5]:


# Data imported correctly.
print(ott.head())
print(ott.dtypes)
print(ott.shape)


# ## 5. Combine the two DataFrames

# In[6]:


# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# View the DataFrame.
print(mov_ott.shape)
mov_ott.head()


# ## 6. Create a lineplot

# In[7]:


# Create a simple lineplot.
sns.lineplot(x='Year', y='IMDb', data=mov_ott)


# In[8]:


# Create a simple lineplot.
sns.lineplot(x='Year', y='IMDb', data=mov_ott, ci=None)


# In[9]:


# Create lineplots with specification.
sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ='Age')


# In[10]:


# Create lineplots with specification.
sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ='Age', ci=None)


# In[ ]:




