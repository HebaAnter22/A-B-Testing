#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px


# In[2]:


control = pd.read_csv('control_group.csv')


# In[3]:


test = pd.read_csv('test_group.csv')


# In[4]:


control.head()


# In[5]:


test.head()


# In[6]:


compined_data = pd.concat([control, test], ignore_index= True)


# In[7]:


compined_data =compined_data.iloc[:,0].str.split(';', expand= True)


# compined_data.head()

# In[8]:


col = ['Campaign Name', 'Date', 'Spend [USD]', 'Impressions', 'Reach',
       'Website Clicks', 'Searches', 'View Content',
       'Add to Cart', 'Purchase']


# In[9]:


compined_data.columns= col


# In[10]:


compined_data.info()


# In[11]:


for feat in compined_data.columns:
    try:
        compined_data[feat] = pd.to_numeric(compined_data[feat])
    except ValueError:
        pass   


# In[12]:


#['Date'] =  pd.to_datetime(compined_data['Date'], format='%d/%m/%Y')


# In[13]:


for feat in compined_data.columns:
    try:
        compined_data[feat].fillna(value=compined_data[feat].mean(), inplace=True)
    except TypeError:
        pass    


# In[14]:


compined_data.head()


# In[15]:


for feat in compined_data.columns:
       counts = compined_data.groupby('Campaign Name')[feat].sum()
       x_axis = ['Control', 'Test']
       if compined_data[feat].dtype == 'int64':
           figure = px.bar(data_frame = compined_data,  x= x_axis, y= counts, color= x_axis, title= feat, 
                           height=400, width=400, labels=dict(x=" ", y=feat, color="Campaign Name"))
           figure.show()

       elif compined_data[feat].dtype == 'float64':
           figure = px.bar(data_frame = compined_data,  x= x_axis, y= counts, color= x_axis, title=feat,
                           height=400, width=400, labels=dict(x=" ", y=feat, color="Campaign Name"))
           figure.show()
       else:
           pass
  

       


# In[16]:


figure = px.scatter(data_frame = compined_data, 
                    x="Impressions",
                    y="Spend [USD]", 
                    size="Spend [USD]", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# In[17]:


figure = px.scatter(data_frame = compined_data, 
                    x="Searches",
                    y="Website Clicks", 
                    size="Spend [USD]", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# In[18]:


figure = px.scatter(data_frame = compined_data, 
                    x="Add to Cart",
                    y="View Content", 
                    size="Add to Cart", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# In[19]:


figure = px.scatter(data_frame = compined_data, 
                    x="Add to Cart",
                    y="Purchase", 
                    size="Purchase", 
                    color= "Campaign Name", 
                    trendline="ols")
figure.show()


# In[20]:


total_purchase = compined_data.groupby('Campaign Name')['Purchase'].sum()
total_spent = compined_data.groupby('Campaign Name')['Spend [USD]'].sum()
Campaign_Name = ['Control', 'Test']
purchase_per_money_spent = total_purchase/total_spent
figure = px.bar(data_frame = purchase_per_money_spent, x= Campaign_Name, y= purchase_per_money_spent,
                color= Campaign_Name, title= 'Purchase per Dollar Spent', height=400, width=400, 
                labels=dict(x=" ", y= " ", color="Campaign Name"))
#figure= px.pie(compined_data, values= purchase_per_money_spent, names=Campaign_Name, title='Purchase per Total Money Spent')
figure.show()


# In[21]:


figure = px.line(data_frame = compined_data, 
                    x="Date",
                    y="Impressions", 
                    color= "Campaign Name")
figure.show()


# In[22]:


for feat in compined_data.columns:
   
       
       if compined_data[feat].dtype == 'int64':
           figure = px.box(data_frame = compined_data,  y= feat, color= "Campaign Name", title= feat, 
                           height=400, width=400, labels=dict(x=" ", y=feat, color="Campaign Name"))
           figure.show()

       elif compined_data[feat].dtype == 'float64':
           figure = px.box(data_frame = compined_data, y=  feat, color= "Campaign Name", title=feat,
                           height=400, width=400, labels=dict(x=" ", y=feat, color="Campaign Name"))
           figure.show()
       else:
           pass


# In[23]:


compined_data[(compined_data['View Content']==4219) & (compined_data['Searches'] ==4891)]


# In[24]:


compined_data.groupby('Campaign Name')['Impressions'].mean()


# In[25]:


compined_data.groupby('Campaign Name')['Spend [USD]'].mean()

