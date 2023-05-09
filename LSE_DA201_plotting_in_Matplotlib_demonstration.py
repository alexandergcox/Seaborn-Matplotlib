#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Plotting in Matplotlib (tutorial video)

# This file contains the code snippets that are introduced in the Plotting in Matplotlib video. 
# Follow along with the demonstration to:
# - create an plot
# - add lines to a plot
# - create multiple plots in one figure
# - change plot background colours.
# 
# Play and pause the video to follow along with the demonstration.

# ### 1. Import Matplotlib

# In[1]:


# Import Matplotlib as plt.
import matplotlib.pyplot as plt


# ### 2. Create an empty plot

# In[2]:


# Creat an empty plot with the subplots() function.
fig, ax = plt.subplots()


# ### 3. Add lines to a plot

# In[3]:


# Draw a line by specifying the axes.
ax.plot([1, 2, 3, 4], [8, 6, 4, 2])

# View the figure.
fig


# In[4]:


# Draw a line by specifying the axes.
ax.plot([8, 6, 4, 2], [1, 2, 3, 4])

# View the figure.
fig


# ### 4. Create a single figure with multiple plots

# In[5]:


# Create a 2 x 2 figure by specifying the nrows and ncols parameters.
fig2, ((top_left, top_right), (bottom_left, bottom_right)) = plt.subplots(2, 2)


# ### 5. Specify plot axes 

# In[6]:


# Specify each variable.
top_left.plot([1, 2, 3, 4], [1, 1, 1, 1], color='blue')
top_right.plot([1, 2, 3, 4], [1, 1, 1, 1], color='red')
bottom_left.plot([1, 2, 3, 4], [1, 1, 1, 1], color='black')
bottom_right.plot([1, 2, 3, 4], [1, 1, 1, 1], color='orange')

# View the figure.

fig2


# ### 6. Change the background colour

# In[7]:


# Set the background colour of the figure.
fig2.set_facecolor('yellow')

# View the figure.
fig2


# In[ ]:




