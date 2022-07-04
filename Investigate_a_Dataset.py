#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [TMDb_movie]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# # <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# This data set contains information about 10,000 movies collected from the Movie Database (TMDb), including user ratings and revenue.
# 
# 
# ● Certain columns, like ‘cast’ and ‘genres’, contain multiple values separated by pipe (|)
# characters.
# 
# 
# ● There are some odd characters in the ‘cast’ column. Don’t worry about cleaning them. You can
# leave them as is.
# 
# 
# ● The final two columns ending with “_adj” show the budget and revenue of the associated movie in terms of 2010 dollars,accounting for inflation over time.
# 
# ### Question(s) for Analysis
# Which year has the highest release of movies? 
# 
# What kinds of properties are associated with movies that have high revenues?
# 
# Which Genre Has The Highest Release  of movies ?
# 

# In[28]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


# Upgrade pandas to use dataframe.explode() function. 
get_ipython().system('pip install --upgrade pandas==0.25.0')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# >  In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you document your steps carefully and justify your cleaning decisions.
# 
# ### General Properties
# >loading Data and information and the shape of rows and columns 
# >make data describtion 

# In[30]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.

df =pd.read_csv('tmdb-movies.csv')

df.head()


# In[31]:


# no. of rows and columns 
df.shape


# no. of rows = 10866
# 
# 
# no. of columns = 21

# In[32]:


df.describe()


# 
# max revenue = 2.781506e+09 
# min revenue = 0.000000
# mean revenue = 3.982332e+07
# 
# last release year is 2015 
# 
# min budget = 0.000000e
# mean budget = 1.462570e+07
# max budget = 4.250000e+08
# 
# max vote average = 9.200000   
# min vote average 1.500000   
# 

# In[33]:


df.info()


# In[34]:



df.nunique()


# # Cleaning data
# In this step we will remove duplcated rows , then drop the columns which I don't need them in my analyzing. after that , I will make a distribuation to each properties .

# Removing the null values to make correct analyzing 

# In[35]:


df.isnull().sum()


# In[36]:


df.fillna(0)
print()


# Duplicate the rows 

# In[37]:


df.duplicated().sum()


# In[38]:


df.drop_duplicates(inplace=True)
df.shape


# Remove the sections which i don't need in my analyzing

# In[39]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.
df.drop(['homepage', 'director', 'tagline','overview','revenue_adj','budget_adj','imdb_id'], axis = 1, inplace = True)
df.head()

df.info()
df['release_year'].plot.hist();
plt.xlabel('years ')
plt.ylabel(' no. of movies')
plt.title('no. of movies through years ')


# from the distribution above :
# 
# most of the movies are produced after year (2000).
# 

# # Which year has the highest release of movies? 

# In[40]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
df.genres.value_counts().plot(kind='bar',alpha=0.5, color= 'blue', label='genres')
df.release_year.value_counts().plot(kind='bar',alpha=0.5, color= 'red', label='release_year')

plt.xlabel('years ')
plt.ylabel(' genres')
plt.title('year with highest release')
plt.legend();

year=df.groupby('release_year').count()['id']
print(year.tail())


# The year which have the highest release of movies is 2014
# 
# The year which have the lowest release of movies is 1961

# # What kinds of properties are associated with movies that have high revenues?

# In[41]:


df.plot.scatter(x='revenue', y='budget',title =' revenue : budget', figsize =(8,8))
df.plot.scatter(x='revenue', y='popularity',title =' revenue : popularity', figsize =(8,8))
df.plot.scatter(x='revenue', y='runtime',title =' revenue : runtime', figsize =(8,8))
df.plot.scatter(x='revenue', y='vote_average',title =' revenue : voteaverage', figsize =(8,8))


# from charts the movie with high budget have high revenues .

# # Which Genre Has The Highest Release  of movies ?

# In[42]:


# first make a list , then the genres have alot of categories we will seperate them with split ,then put them in the list
line = []
for genre in df['genres']:
    genre= df['genres'].str.cat(sep = '|').split('|')
    line= pd.Series(genre)
# we will plot every category 
line.value_counts().plot(kind='bar',alpha=0.5, color= 'Green', label='Genre')
plt.title("Genre With Highest Release",fontsize=20)
plt.xlabel('Movies',fontsize=20)
plt.ylabel("Genres",fontsize= 20)


# Drama has the highest release with above 4000  release then comedy with  above 3000 release.

# <a id='conclusions'></a>
# ## Conclusions
# 
# from data analyzing :
# 
# > After 2000 year the production is very high .
# 
# > Drama has the highest release genre .
# 
# > 2014 is the year with high realse of movies.
# 
# > The best factor  to increase revenue is the budget of the movie.
# 
# 
# 
# Limitations:Data analysis depend on clear data, there is a lot of factor effect on this.
# The missing values affect on data and give false results also (null, zero values ), therefore, we clean data from these values.
# The data with different data types affect our data and must be changed to make true results.
# ## Submitting your Project 
# 
# > **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > **Tip**: Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[ ]:





# In[43]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:





# In[ ]:





# In[ ]:




