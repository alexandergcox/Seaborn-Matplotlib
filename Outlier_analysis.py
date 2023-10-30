# Outlier analysis

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app that provides recommendations based on the last movie you watched. As a part of their process, they want to review the data and gather enough information before they start making suggestions and recommendations to their clients. 
# 
# This analysis uses the `movies.csv` and `ott.xlsx` data sets. Based on the available information, in this activity you will:
# 
# - perform an outlier analysis on the data to detect outliers or anomalies and find interesting relationships among the variables
# - understand what the data says by visualising it on a boxplot.

# ## 1. Import the libraries

# In[1]:


# Import necessary libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ## Import Excel file

# In[2]:


# Load the Excel data using pd.read_excel.
ott = pd.read_excel('ott.xlsx')

# View the columns.
print(ott.columns)


# ## Import CSV file

# In[3]:


# Load the CSV data using pd.read_csv.
movies = pd.read_csv('movies.csv')

print(movies.columns)


# ## Validate the DataFrames

# In[4]:


# Data imported correctly?
print(movies.head())
print(movies.shape)
print(movies.dtypes)


# In[5]:


# Data imported correctly?
print(ott.head())
print(ott.dtypes)
print(ott.shape)


# ## Combine the two DataFrames

# In[6]:


# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on = 'ID')

# View the DataFrame.
print(mov_ott.shape)
mov_ott.head()


# ## 2. Create a boxplot

# In[7]:


# Create boxplot with two variables (Age and IMDb).
sns.boxplot(x='Age', y='IMDb', data=mov_ott)


# In[ ]:




