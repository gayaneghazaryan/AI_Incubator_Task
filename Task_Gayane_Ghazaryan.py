#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


# In[17]:


source1 = requests.get("https://randomuser.me/api/?results=5000").json()
source2 = requests.get("https://randomuser.me/api/?results=5000").json()


# In[18]:


result = source1["results"] + source2["results"]
df = pd.DataFrame(result)


# In[19]:


df.head()


# In[20]:


#bar chart of user nationalities
barplt1 = df['nat'].value_counts().plot(kind = 'bar', title = "Nationality bar chart")
barplt1.set_xlabel("Nationalities")
barplt1.set_ylabel("Frequency")


# In[21]:


#histogram for user age
lst1 = [d['age'] for d in df['dob']]
plt.hist(lst1, bins = 20, edgecolor = "black")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.title("Age Histogram")


# In[22]:


#piechart of user gender
df['gender'].value_counts().plot(kind = 'pie')


# In[23]:


#bar chart for username length
lst2 = [len(d['username']) for d in df['login']]
dict1 = Counter(lst2)
plt.bar(list(dict1.keys()), list(dict1.values()))
plt.xlabel("Length of username")
plt.ylabel("Frequency")
plt.title("Username length frequencies")


# In[24]:


#box plot for gender and age relation
lst3 = [d for d in df['gender']]
dict2 = {'Gender':lst3, 'Age':lst1}
df1 = pd.DataFrame(dict2)
sns.boxplot(x = 'Gender', y = 'Age', data = df1)


# In[25]:


#Scatter plot for age of registration and password length
lst4 = [d['age'] for d in df['registered']]
lst5 = [len(d['password']) for d in df['login']]
plt.scatter(lst4, lst5)


# In[27]:


#Bar chart for timezone frequency
lst6 = [d['timezone']['offset'] for d in df['location']]
dict2 = Counter(lst6)
plt.bar(list(dict2.keys()), list(dict2.values()))
plt.xlabel("Timezone")
plt.ylabel("Frequency")
plt.title("Timezone frequencies")
plt.figure(figsize = (200, 80), dpi = 80)

plt.show()


# In[ ]:




