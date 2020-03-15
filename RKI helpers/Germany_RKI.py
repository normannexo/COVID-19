#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import datetime
import numpy as np
import os

#dir_path = os.path.dirname(os.path.abspath(__file__))
dir_path = '.'

csv_file = os.path.join(dir_path, 'csv', 'archiv', 'rki_' + now.strftime('%Y-%m-%d_%H_%M') + '.csv')
CSVLOC=os.path.join(dir_path, 'csv', 'archiv')


# In[35]:


df_data = pd.DataFrame()
for item in os.listdir(CSVLOC):
    if os.path.isfile(CSVLOC + '/' + item):
        df_data = pd.concat([df_data,pd.read_csv(CSVLOC + '/' + item,  parse_dates=True)])
        print("added "+ CSVLOC + "/" + item + " to data frame.")
    else:
        print(item + " is no file")
df_data
df_data['date']=pd.to_datetime(df_data.date)
df_data['date'] = df_data.date.dt.strftime('%Y-%m-%d')
df_data['deaths'] = df_data.confirmed.str.extract(r'\((\d+)\)')
df_data['confirmed'] = df_data.confirmed.str.replace(r'(\d+) \(\d+\)', r'\1')
df_data.deaths.replace({np.nan:0}, inplace=True)
df_data = df_data.drop('Unnamed: 0', axis=1)
df_data.drop_duplicates()
df_data['date'] =pd.to_datetime(df_data.date)
df_data = df_data.drop(df_data[df_data.Bundesland=='Gesamt'].index)


# In[36]:


df_data.to_csv('./csv/rki_data.csv')


# In[ ]:


print(df_data)

