#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Create plots with Seaborn

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app that provides recommendations based on the last movie you watched. As a part of their process, they want to analyse the data and gather enough information before they start making suggestions and recommendations to their clients. 
# 
# This analysis uses the `movies.csv` and `ott.xlsx` data sets. Based on the available information, in this activity you will:
# 
# - perform an exploratory analysis on the data to identify underlying patterns within the data, detect outliers or anomalies, and find interesting relations among the variables
# - understand the narrative by plotting a countplot, a histogram, and a scatterplot.

# ## 1. Import the libraries

# In[2]:


# Import Pandas, Seaborn, and Matplotlib.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ## 2. Import Excel file

# In[3]:


# Load the Excel data using pd.read_excel.
ott = pd.read_excel('ott.xlsx')

# View the columns.
print(ott.columns)


# ## 3. Import CSV file

# In[4]:


# Load the CSV data using pd.read_csv.
movies = pd.read_csv('movies.csv')

# View the columns.
print(movies.columns)


# ## 4. Validate the DataFrames

# In[5]:


# Data imported correctly?
print(movies.head())
print(movies.shape)
print(movies.dtypes)


# In[6]:


# Data imported correctly?
print(ott.head())
print(ott.dtypes)
print(ott.shape)


# ## 5. Combine the two DataFrames

# In[7]:


# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# View the DataFrame.
print(mov_ott.shape)
mov_ott.head()


# ## 6. Create a countplot

# In[8]:


# Create a countplot based on number of movies streamed by Netflix per age group.
sns.countplot(x='Age', hue='Netflix', data=mov_ott)


# ## 7. Create a histogram

# In[9]:


# Create a histogram based on IMDb. 
sns.histplot(data=mov_ott, x='IMDb', binwidth=1)


# ## 8. Create a scatterplot

# In[10]:


# Create a scatterplot with two variables (IMDb and Rotten Tomatoes).
sns.scatterplot(x='IMDb', y='Rotten Tomatoes', data=mov_ott)


# In[ ]:




