
"""pandasplotcode.ipynb

# An Introduction to Data Visualization with Pandas

## Importing the libraries
"""

import matplotlib
matplotlib.rcParams['figure.facecolor'] = 'white'

# Commented out IPython magic to ensure Python compatibility.
# The first line is only required if you are using a Jupyter Notebook
# %matplotlib inline    
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Getting the data"""

url='https://raw.githubusercontent.com/alanjones2/ajbooks/main/data/londonweather2018.csv'
weather = pd.read_csv(url, index_col='Month')
print(weather)

"""## A first Pandas Plot"""

weather.plot(y='Tmax')
plt.show()

"""## Simple charts"""

weather.plot(y=['Tmax','Tmin'])
plt.show()

weather['Tmed'] = (weather['Tmax'] + weather['Tmin'])/2

weather.plot(y=['Tmax','Tmin','Tmed'])
plt.show()

"""### Bar Charts"""

weather.plot(kind='bar', y='Rain')
plt.show()

weather.plot(kind='barh', y='Rain')
plt.show()

weather.plot(kind='bar', y=['Tmax','Tmin'])
plt.show()

weather.plot(kind='bar', y=['Tmax','Tmed','Tmin'])
plt.show()

"""### Scatter Plot"""

weather.plot(kind='scatter', x='Sun', y='Rain')
plt.show()

import seaborn as sns
sns.regplot(data=weather, x='Sun', y='Rain', ci=False)

"""### Pie charts"""

weather.plot(kind='pie', y='Sun')
plt.show()

weather.plot(kind='pie', y = 'Sun', legend=False)
plt.show()

"""## Statistical charts and spotting unusual events"""

more_weather = pd.read_csv('https://raw.githubusercontent.com/alanjones2/ajbooks/main/data/londonweather.csv')

print(more_weather.Rain.describe())

more_weather.plot.box(y='Rain')
plt.show()

"""## Histograms"""

more_weather.plot(kind='hist', y='Rain')
plt.show()

"""#### More bins"""

more_weather.plot(kind='hist', y='Rain', bins=[0,25,50,75,100,125,150,175])
plt.show()

more_weather.plot.hist(y='Rain', bins=[0,25,75,175])
plt.show()

"""## Pandas Plot utilities

### Multiple charts
"""

weather.plot(subplots=True)
plt.show()

weather.plot(y=['Tmax','Tmin','Rain','Sun'],subplots=True,layout=[2,2],figsize=[10,5])
plt.show()

weather.plot(kind='bar', y=['Tmax', 'Tmin','Rain','Sun'], subplots=True, layout=(2,2), figsize=(10,5))
plt.show()

weather.plot(kind='pie', subplots=True, legend=False, layout=(3,2), figsize=(10,10))
plt.show()

"""### Saving the Charts"""

weather.plot(kind='pie', y='Rain', legend=False)
plt.show()
plt.savefig("pie.png")

"""# Customizing Pandas Plots and Charts"""

weather.plot(y='Tmax')
plt.show()

"""## Change the size and color

"""

weather.plot(y='Tmax', figsize=(8,5), color='Red')
plt.show()

"""# Setting a title"""

weather.plot(y='Tmax', title='Maximum temperatures')
plt.show()

"""## Display a grid"""

weather.plot(y='Tmax', grid=True)
plt.show()

"""## Changing the legend

"""

weather.plot(y='Tmax', legend=False)
plt.show()

weather.plot(y='Tmax', label='Max Temp')
plt.show()

"""## Customize the ticks"""

weather.plot(y='Tmax', xticks=(0,1,2,3,4,5,6,7,8,9,10,11), yticks=(0,10,20,30))
plt.show()

weather.plot(y='Tmax', xticks=(1,3,5,7,9,11), yticks=(0,10,20,30))
plt.show()

weather.plot(y='Tmax', xticks=())
plt.show()

plot = weather.plot(y='Tmax', xticks=range(0,12), fontsize=18)
plt.show()

plot = weather.plot(y='Tmax', xticks=range(1,13), fontsize=18, rot=90)
plt.show()

"""## It could get messy

"""

plot_kwargs={'xticks':range(0,12),
  'yticks':(0,10,20,30),
  'grid':True,
  'fontsize':12,
  'rot':45}

weather.plot(y='Tmax', **plot_kwargs)
plt.show()

weather.plot(y=['Tmin','Tmed','Tmax'], **plot_kwargs)
plt.show()

plot_kwargs['xticks']=range(0,12)
weather.plot.bar(y=['Tmin','Tmed','Tmax'], **plot_kwargs)
plt.show()