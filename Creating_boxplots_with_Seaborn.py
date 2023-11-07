# Creating boxplots with Seaborn (tutorial video)


# - create a boxplot using Seaborn
# - create a boxplot with a third variable
# - specify the order of variables in a boxplot.


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


# ### 2. Create a boxplot

# In[2]:


# Create a boxplot based on species and body_mass_g.
sns.boxplot(data=penguins, x='species', y='body_mass_g')


# ### 3. Create a boxplot with a third variable

# In[3]:


# Create a boxplot based on species, body_mass_gm and sex.
sns.boxplot(data=penguins, x='species', y='body_mass_g', hue='sex')


# ### 4. Specify the order of variables

# In[4]:


# Specify the order of variables with the groupby() function.
my_order = penguins.groupby(by=['species'])['body_mass_g'].median().iloc[::-1].index

# Create a boxplot based on the order of variables.
sns.boxplot(x='species', y='body_mass_g', data=penguins, order=my_order)


# In[ ]:




