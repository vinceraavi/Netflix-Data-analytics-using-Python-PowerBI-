#!/usr/bin/env python
# coding: utf-8

# In[34]:


#importing the dataset
import pandas as pd
data = pd.read_csv(r"D:\DATA SCIENCE\SQL\SQL projects\Netflix sql project\Netflix data set.csv")


# In[35]:


data


# In[36]:


data.head() #To get top 5 rows from the data set


# In[37]:


data.tail() #to get last 5 rows from dataset


# In[38]:


data.shape #to get no. of rows and columns


# In[39]:


data.size #to get total elements of the dataset


# In[40]:


data.columns #to get columns names of the data set


# In[41]:


data.dtypes


# In[42]:


data.info() #to show indexes,columns,data-types,memory info of the dataset basically all details


# # Task 1: Remove any duplicates if there in the record in the dataset

# ## Duplicate()

# In[43]:


data.head()


# In[44]:


data.shape


# In[45]:


#to check row wise and detect the duplicate rows
data[data.duplicated()]


# In[46]:


#to remove duplicate rows
data.drop_duplicates(inplace = True)


# In[47]:


data[data.duplicated()] 


# In[48]:


data.shape


# # Task 2: To check Null Values in any column and show it with a heat map

# ## isnull()

# In[49]:


data.head()


# In[50]:


data.isnull()


# In[51]:


data.isnull().sum()


# In[52]:


import seaborn as sns   #To import seaborn library


# In[53]:


sns.heatmap(data.isnull())    #using heatmap show null values count


# # Q1. For "House of Cards", Who is the director and what is the show Id?

# ## isin()

# In[54]:


data.head()


# In[55]:


data[data['Title'].isin(['House of Cards'])]


# In[56]:


data[data['Title'].str.contains('House of Cards')]


# # Q2. In which year highest number of the TV Shows & Movies were released? Show with Bar graph?

# ## dtypes

# In[57]:


data.dtypes


# ## to_datetime

# In[58]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[59]:


data.dtypes


# ## dt.year.value_counts()

# In[60]:


data['Date_N'].dt.year.value_counts()   #It counts the occurence of all inviduals years in date column


# ## Bar Graph

# In[61]:


data['Date_N'].dt.year.value_counts().plot(kind="bar")


# ## Q3.How many movies and tv shows are in this dataset?show with Bar Graph.

# ### groupby()

# In[62]:


data.head(2)


# In[63]:


data.groupby('Category').Category.count()  #To group all unique items of a column and show their count.


# In[64]:


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a Pandas DataFrame 'data' with a column 'Category'
# You can count the unique values in the 'Category' column
category_counts = data['Category'].value_counts()

# Create a count plot using Seaborn
plt.figure(figsize=(10, 6))  # Optional: set the figure size
sns.countplot(data=data, x='Category', order=category_counts.index, palette="Set2")

# Optional: Customize the plot
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.xlabel('Category', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Count of Unique Values in Category Column', fontsize=14)

# Show the plot
plt.show()


# ## Q4. Show all the Movies that were released in year 2000

# In[65]:


data.head(2)


# In[66]:


data['Year'] = data['Date_N'].dt.year


# In[67]:


data.head(2)


# ## Filtering

# In[68]:


data[(data['Category'] == 'Movie')&(data['Year']==2000)]


# In[69]:


data[(data['Category'] == 'Movie')&(data['Year']==2020)]


# ## Q5. Show only the Titles of all TV Shows that were released in India only.

# ### Filtering

# In[70]:


data.head(2)


# In[75]:


data[(data['Category']== 'TV Show') & (data['Country'] == 'India')] ['Title']


# ## Q6. Show top 10 Directors,who gave the highest number of TV Shows & Movies to Netflix? 

# ### value_counts()

# In[77]:


data.head(2)


# In[79]:


data['Director'].value_counts().head(10)


# ## Q7.Show all the records,Where "Category is Movie and type is Comedy" or "Country is United Kingdom".

# ### Filtering (And, Or Operators)

# In[84]:


data[(data['Category']=='Movie')&(data['Type']=='Comedies')]


# In[95]:


data[(data['Category'] == 'Movie') & (data['Type']=='comedies') | (data['Country'] == 'United Kingdom')]


# ## Q8. In how many movies/shows, Tom Cruise was cast?

# In[97]:


data.head(2)


# ### filtering

# In[99]:


data[data['Cast'] == 'Tom Cruise']


# ### str.contains()

# In[100]:


data[data['Cast'].str.contains('Tom Cruise')]


# ### Creating a new data-frame

# In[101]:


data_new = data.dropna()


# In[102]:


data_new.head(4)


# In[104]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ## Q9. What are the different Ratings defined by Netflix?

# ### nunique()

# In[107]:


data.head(3)


# In[105]:


data.Rating.nunique()


# ### unique()

# In[106]:


data.Rating.unique()


# ### Q.9.1. How many Movies got the "TV-14" rating, in Canada?

# In[109]:


data.head(3)


# In[112]:


data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14')]


# In[127]:


data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14')].shape


# In[128]:


data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14') & (data['Country']== 'Canada')].shape


# ### Q.9.2. How many TV Shows got the 'R' rating, after year 2018?

# In[129]:


data.head(3)


# In[132]:


data[(data['Category']=='TV Show') & (data['Rating'] == 'R')]


# In[133]:


data[(data['Category']=='TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]


# ## Q10. What is the maximum duration of a Movie/Show on Netflix?

# In[134]:


data.head(3)


# In[136]:


data["Duration"].unique()


# In[137]:


data.Duration.dtypes


# #### str.split()

# In[140]:


data[['Minutes','Unit']] = data['Duration'].str.split(' ',expand=True)


# In[141]:


data.head(3)


# ### max()

# In[142]:


data.Minutes.max()


# In[143]:


data.Minutes.min()


# In[144]:


data.Minutes.mean()


# In[145]:


data.dtypes


# ## Q11. Which individual country has the Highest No. of TV Shows?

# In[146]:


data.head(2)


# In[147]:


data_tvshow = data[data['Category'] == 'TV Show']


# In[148]:


data_tvshow.head(3)


# In[152]:


data_tvshow.Country.value_counts().head(1)


# ## Q12.How can we sort the dataset by Year?

# In[153]:


data.head(2)


# In[156]:


data.sort_values(by="Year")


# In[158]:


data.sort_values(by = 'Year', ascending = False).head(10)


# ## Q13. Find all the instances where:
#     Category is 'Movie' and Type is 'Dramas'
#     or
#     Category is 'TV Show' & Type is 'Kids TV'

# In[159]:


data.head(2)


# In[162]:


data[ (data['Category'] == 'Movie') & (data['Type'] == 'Dramas') ].head(2)


# In[168]:


data[(data['Category']=='TV Show') & (data['Type'] == "Kids' TV") ].head(2)


# In[169]:


data[ (data['Category'] == 'Movie') & (data['Type'] == 'Dramas') | (data['Category']=='TV Show') & (data['Type'] == "Kids' TV") ]


# In[ ]:




