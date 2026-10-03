#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
orders=pd.read_csv(r'D:\Work\Projects\E-commerce Customer & sales analytics\olist_orders_dataset.csv')
payments=pd.read_csv(r'D:\Work\Projects\E-commerce Customer & sales analytics\olist_order_payments_dataset.csv')


# In[6]:


orders['order_purchase_timestamp']=pd.to_datetime(orders['order_purchase_timestamp'])
df=pd.merge(orders,payments,on='order_id')


# In[10]:


today_date=df['order_purchase_timestamp'].max()+pd.Timedelta(days=1)
RFM=df.groupby('customer_id').agg({'order_purchase_timestamp':lambda x:(today_date-x.max()).days,
    'order_id':'count',
    'payment_value':'sum'}).reset_index()
RFM.columns=['customer_id','Recency','Frequency','Monetary']


# In[15]:


def segment(row):
    if row['Recency']<30 and row['Frequency']>2:
        return 'VIP Customer'
    elif row['Recency']<60:
        return 'Regular Customer'
    elif row['Recency']>90:
        return 'Lost Customer'
    else:
        return'Normal Customer'
RFM['segment']=RFM.apply(segment,axis=1)
RFM.to_csv(r'D:\Work\Projects\E-commerce Customer & sales analytics\RFM.New.csv',index=False)
print('RFM created successfully!')
print(RFM.head())


# In[ ]:




