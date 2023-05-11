#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics Using Python

# ## Practical activity: Highlight and annotate plots

# **This is the solution to the activity.**
# 
# Canopy is a new boutique streaming company that is looking to create an app that provides recommendations based on the last movie you watched. As a part of their process, they want to review the data and gather enough information before they start making suggestions and recommendations to their clients. 
# 
# This analysis uses the `movies.csv` and `ott.xlsx` data sets. Based on the available information, in this activity you will:
# 
# - customise the existing scatter, box, and lineplots
# - add more customisations to extract further information from the scatterplots and countplots.

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


# Data imported correctly?
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


# ## 6. Create a countplot

# In[7]:


# Create a countplot based on number of movies streamed by Netflix per age group.
sns.countplot(x='Age', hue='Netflix', data=mov_ott)


# ## 7. Create a histogram

# In[8]:


# Create a histogram based on IMDb. 
sns.histplot(data=mov_ott, x='IMDb', binwidth=1)


# ## 8. Create a scatterplot

# In[9]:


# Create scatterplot with two variables (IMDb and Rotten Tomatoes).
sns.scatterplot(x='IMDb', y='Rotten Tomatoes', data=mov_ott)


# ## 9. Create a lineplot

# In[10]:


# Create a simple lineplot.
sns.lineplot(x='Year', y='IMDb', data=mov_ott)


# In[11]:


# Create a simple lineplot.
sns.lineplot(x='Year', y='IMDb', data=mov_ott, ci=None)


# In[12]:


# Create lineplots with specification.
sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ="Age")


# In[13]:


# Create lineplots with specification.
sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
             hue ='Age', ci=None)


# ## 10. Customise plots

# ### Barplot

# In[14]:


mov_ott_2010 = mov_ott[mov_ott['Year']>=2010]

ax = sns.countplot(x='Year', data=mov_ott_2010)

ax.set(ylabel='Percent')

total = len(mov_ott_2010['Year'])

for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x()
    y = p.get_y() + p.get_height()
    ax.annotate(percentage, (x, y))

plt.xticks(rotation=90)
plt.show()


# ### Histogram

# In[15]:


ax = sns.displot(data=mov_ott, x='IMDb', bins=10,kind='hist', 
                 palette='GnBu', aspect=1.4, kde=True)

plt.show()


# ## 11. Highlight and annotate plots

# ### Scatterplot

# In[16]:


sns.scatterplot(data=mov_ott, x='IMDb', y='Rotten Tomatoes', hue='Netflix')

plt.show()


# ### Boxplot

# In[17]:


sns.boxplot(data=mov_ott, x='Age', y='IMDb', linewidth=2, 
            notch=True, hue='Netflix', palette='Set3')

plt.show()


# ### Lineplot

# In[18]:


sns.lineplot(x = 'Year', y = 'IMDb', data=mov_ott, linewidth=0)


# In[19]:


sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])], 
             hue ='Age')


# In[20]:


sns.lineplot(x = 'Year', y = 'IMDb', 
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])], 
             hue ='Age', style = 'Age', markers=True, ci=0)


# In[22]:


sns.lineplot(x = 'Year', y = 'IMDb', data=mov_ott, linewidth=0)

sns.lineplot(x = 'Year', y = 'IMDb',
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])], 
             hue ='Age')

sns.lineplot(x = 'Year', y = 'IMDb', 
             data=mov_ott[mov_ott['Age'].isin(['16+', '18+'])], 
             hue ='Age', style = 'Age', markers=True, ci=0)


# In[ ]:




