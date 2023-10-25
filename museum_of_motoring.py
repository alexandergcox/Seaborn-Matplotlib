# Museum of Motoring History case study

# The Museum of Motoring History is preparing for an exhibition about vehicles from the 1970s. The curator wants to create an interactive exhibit for visitors to learn about the fuel efficiency of many popular cars. They have a data set of car fuel efficiency from 1970 to 1982 in which the fuel efficiency is measured in miles per gallon (MPG). A higher MPG means the car is more efficient. What visualisations could the exhibit include to engage visitors? This is where pointplots can be used as a replacement for bar charts.
# 
# Let’s help the curator! 

# ### 1. Prepare your workstation

# In[1]:


# Import Matplotlib, Seaborn, and Pandas.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read the CSV file.
mpg = pd.read_csv('mpg.csv')

# View the DataFrame.
print(mpg.shape)
print(mpg.dtypes)
print(mpg.columns)
mpg.head()


# ### 2. Create a lineplot

# In[2]:


# Create a lineplot for fuel efficiency.
sns.lineplot(x='model_year', y='mpg', data=mpg)


# ### 3. Create a barplot

# In[3]:


# Create a barplot for fuel efficiency.
sns.barplot(x='model_year', y='mpg', data=mpg)


# ### 4. Create a pointplot

# In[4]:


# Create a pointplot for fuel efficiency.
sns.pointplot(x='model_year', y='mpg', data=mpg)


# In[5]:


# Create a pointplot for fuel efficiency by manufacturing country.
sns.pointplot(x='model_year', y='mpg', hue='origin', data=mpg)


# In[ ]:




