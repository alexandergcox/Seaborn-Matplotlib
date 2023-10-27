# Creating scatterplots with Seaborn 


# - create a scatterplot with two variables
# - create a scatterplot with three variables
# - create a scatterplot with a regression line.
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


# ### 2. Create a scatterplot with two variables

# In[2]:


# Create a single_day variable.
# Specify a chosen day within the ActivityDate column and fitness DataFrame.
single_day = fitness[fitness['ActivityDate'] == '4/12/2016']

# View the output.
print(single_day.shape)

# Create the scatterplot.
sns.scatterplot(x='TotalSteps',
               y='Calories',
               data=single_day)


# ### 3. Create a scatterplot with three variables

# In[3]:


# Create a scatterplot with three variables.
sns.scatterplot(x='TotalSteps', y='Calories',
               marker='o', hue='VeryActiveMinutes',
               size='VeryActiveMinutes', legend='full',
               data=single_day)

# Adjust the legend position on the plot.
plt.legend(bbox_to_anchor=(1.05, 1))


# ### 4. Create a scatterplot with a regression line

# In[4]:


# Create the scatterplot with a regression line.
sns.regplot(x='TotalSteps', y='Calories', data=single_day)


# In[ ]:




