# Time-series plots with Seaborn (Python)

# This Notebook accompanies the 'Time-series plots with Seaborn (Python)' 
# 
# Follow along with the demonstration to learn how to:
# 
# - apply time-series in a real-life scenario to identify trends
# - create a time-series plot in Seaborn
# - understand/read a time-series plot.

# ### 1. Prepare your workstation

# In[1]:


# Import Matplotlib, Seaborn, and Pandas.
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import *

# Read the CSV file.
weather = pd.read_csv('ny_hourly.csv')

# View the DataFrame.
print(weather.shape)
print(weather.dtypes)
print(weather.columns)
weather.head()


# In[2]:


# Import data again with parse.
weather = pd.read_csv('ny_hourly.csv',
                      parse_dates=[['date', 'TimeEST']],
                      usecols=['date', 'TimeEST', 'TemperatureF',
                               'Dew PointF', 'Humidity'])

# View the DataFrame.
weather


# In[3]:


# Use describe function.
weather.describe()


# In[4]:


# Only values bigger than -100.
weather = weather[weather['TemperatureF'] >-100]

# Sort data.
weather = weather.sort_values('date_TimeEST')

# View the DataFrame.
weather


# In[5]:


# How temperature changes over time.
# Seaborn lineplots.
sns.lineplot(x='date_TimeEST', y='TemperatureF',
            data=weather).set_title("Hourly Weather in New York")


# In[6]:


# Dew point.
sns.lineplot(x='date_TimeEST', y='Dew PointF',
            data=weather).set_title("Hourly Weather in New York")


# In[7]:


# Humidity.
sns.lineplot(x='date_TimeEST', y='Humidity',
            data=weather).set_title("'Hourly Weather in New York")


# In[8]:


# Format dates.
fig, ax = plt.subplots()

sns.lineplot(x='date_TimeEST', y='TemperatureF',
             data=weather).set_title("Hourly Weather in New York")

x_labels = weather['date_TimeEST'].dt.strftime('%Y-%m-%d')

ax.set_xticklabels(x_labels, rotation=45)

plt.show()


# In[9]:


# Plotting different variables.
january_data = weather[weather.date_TimeEST < np.datetime64('2016-01-03')]

fig, temp_ax = plt.subplots()
fig.set_size_inches(14, 8)

humidity_ax = temp_ax.twinx()

# Add labels.
temp_ax.set_title("Hourly Temperature in NYC")
temp_ax.set_xlabel("Date & Time")
temp_ax.set_ylabel("Temperature (ºF)")

humidity_ax.set_ylabel("Humidity (%)")

# Change date and time.
major_locator = AutoDateLocator()
formatter = ConciseDateFormatter(major_locator)
humidity_ax.xaxis.set_major_formatter(formatter)
temp_ax.xaxis.set_major_formatter(formatter)

temp_lines = temp_ax.plot(january_data.date_TimeEST, january_data.TemperatureF, 'r')
humidity_lines = humidity_ax.plot(january_data.date_TimeEST, january_data.Humidity, 'c')


# In[10]:


# Plot multiple variables with the same x-axis.
fig, axes = plt.subplots(nrows=3)
nyc_fig = fig
fig.set_size_inches(14, 10)

temp_lines = axes[0].plot(weather.date_TimeEST, weather.TemperatureF, 'r')
humidity_lines = axes[1].plot(weather.date_TimeEST, weather.Humidity, 'c')
dew_point_lines = axes[2].plot(weather.date_TimeEST, weather['Dew PointF'], 'g')

axes[0].set_xticklabels([])
axes[1].set_xticklabels([])

major_locator = AutoDateLocator()
formatter = ConciseDateFormatter(major_locator)
axes[2].xaxis.set_major_formatter(formatter)
axes[0].set_ylabel("Temperature (ºF)")
axes[1].set_ylabel("Humidity (%)")
axes[2].set_ylabel("Dew Point (ºF)")
axes[2].set_xlabel("Date")
fig.suptitle("Weather in New York City", fontsize=16, y=0.92)
axes[2].legend(temp_lines + humidity_lines + dew_point_lines, 
                ['Temperature', 'Humidity', 'Dew Point'], loc='lower right', ncol=3)


# In[11]:


# Alternative methods.
fig, ax = plt.subplots(2)
fig.set_size_inches(14, 10)

# Create lineplots.
sns.lineplot(x='date_TimeEST',
             y='TemperatureF',
             ax=ax[0],
             data=weather)

sns.lineplot(x='date_TimeEST',
             y='Humidity',
             ax=ax[1],
             data=weather)

# View the lineplots.
plt.show()


# In[ ]:




