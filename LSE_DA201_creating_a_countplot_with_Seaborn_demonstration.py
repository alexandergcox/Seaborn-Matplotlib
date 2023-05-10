#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Creating a countplot with Seaborn (tutorial video)

# This file contains the code snippets that are introduced in the Creating a countplot with Seaborn video. 
# Follow along with the demonstration to:
# - create a countplot
# - display the plot bars horizontally
# - add colour as a third variable.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import libraries and create a DataFrame

# In[2]:


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


# ### 2. Create a countplot of the number of penguins on each island

# In[3]:


# Create a countplot using 'island' and 'penguins' as parameters. 
sns.countplot(x='island', data=penguins)


# ### 3. Display the bars horizontally

# In[4]:


# Assign 'island' to 'y' to flip the plot bars.
sns.countplot(y='island', data=penguins)


# ### 4. Add colour as a third variable

# In[5]:


# Add 'species' as a third variable assigned to colour.
sns.countplot(x='island', hue='species', data=penguins)


# In[ ]:




