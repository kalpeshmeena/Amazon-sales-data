#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[9]:


df=pd.read_csv('Amazon Sale Report.csv',encoding='unicode_escape')


# In[10]:


df.shape


# In[11]:


df.head()


# In[12]:


df.tail()


# In[13]:


df.head()


# In[14]:


df.info()


# In[17]:


#drop unwanted columns
df.drop(['New','PendingS'],axis =1,inplace=True)


# In[19]:


df.info()


# In[20]:


pd.isnull(df)


# In[22]:


pd.isnull(df).sum()


# In[23]:


df.shape


# In[25]:


#drop null values
df.dropna(inplace=True)


# In[26]:


df.shape


# In[27]:


df.columns


# In[28]:


#change the dataType
df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[29]:


df['ship-postal-code'].dtype


# In[31]:


df['Date']=pd.to_datetime(df['Date'])


# In[32]:


df.info()


# In[34]:


#rename columns
df.rename(columns={'Qty':'Quantity'})


# In[35]:


df.describe()


# In[36]:


df.describe(include='object')


# In[37]:


df[['Qty','Amount']].describe()


# ## EDA 

# In[38]:


df.columns


# ## size

# In[40]:


ax=sns.countplot(x='Size',data=df)


# In[42]:


ax=sns.countplot(x='Size',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# #### Note:from above graph we can say most of the people buy M size.

# ### Group by

# In[43]:


df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[44]:


S_Qty=df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)
sns.barplot(x='Size',y='Qty',data=S_Qty)


# ### Note=from above graph you can se most of Qty buys M-Size

# ## Courier Status

# In[51]:


sns.countplot(data= df,x='Courier Status',hue='Status')


# In[49]:


plt.figure(figsize=(10,5))
ax=sns.countplot(data=df,x='Courier Status',hue='Status')
plt.show()


# In[52]:


#histogram
df['Size'].hist()


# In[60]:


df['Category'] =df['Category'].astype(str)
column_data=df['Category']
plt.figure(figsize=(10,5))
plt.hist(column_data,bins=30,edgecolor='Black')
plt.xticks(rotation=45)
plt.show()


# ### from above graph can you see most of the buyer are T-shirt

# In[61]:


#cheking b2b Data by using pi chart
B2B_check= df['B2B'].value_counts()

#plot the pie Chart
plt.pie(B2B_check,labels=B2B_check,autopct='%1.1F%%')

plt.show()


# In[63]:


B2B_check=df['B2B'].value_counts()
#plot the pie Chart
plt.pie(B2B_check,labels=B2B_check.index,autopct='%1.1F%%')

plt.show()


# ### From above pie chart shows that maximum i.e 99.3% of buyers are retailers and 0.8% are B2B buyers.

# In[69]:


#  Prepare data for pie chart
a1 = df['Fulfilment'].value_counts()

# Step 4: Plot the pie chart
fig, ax = plt.subplots()

ax.pie(a1, labels=a1.index, autopct='%1.1f%%', radius=0.7, wedgeprops=dict(width=0.6))
ax.set(aspect="equal")

plt.show()


# In[70]:


# Prepare data for scatter plot
x_data = df['Category']  
y_data = df['Size'] 

# Plot the scatter plot
plt.scatter(x_data, y_data)
plt.xlabel('Category ')  
plt.ylabel('Size')  
plt.title('Scatter Plot') 
plt.show()


# In[71]:


# Plot count of cities by state
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[72]:


# top_10_States 
top_10_state = df['ship-state'].value_counts().head(10)
# Plot count of cities by state
plt.figure(figsize=(12, 6))
sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of  State')
plt.xticks(rotation=45)
plt.show()


# ### Note: From above Graph you can see that most of the buyers are Maharashtra state
# ## Conclusion
# #### The data analysis reveals that the business has a significant customer base in Maharashtra state, mainly serves retailers, fulfills orders through Amazon, experiences high demand for T-shirts, and sees M-Size as the preferred choice among buyers.

# In[ ]:




