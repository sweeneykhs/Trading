#!/usr/bin/env python
# coding: utf-8

# In[10]:


import warnings; warnings.simplefilter('ignore')

import pandas as pd
from pandas import DataFrame
import csv
import math
import numpy as np
from pandas.plotting import autocorrelation_plot
import yfinance as yf
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.pyplot import figure
import datapackage
from numpy import linspace
import datetime
import sklearn
from sklearn.metrics import mean_squared_error
import copy
from statsmodels.tsa.arima.model import ARIMA
import json
# import pandas.tools
from pandas.plotting import lag_plot
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json(orient='records')
        return json.JSONEncoder.default(self, obj)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os


# In[11]:


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds= {
  "type": "service_account",
  "project_id": "trademaster5000",
  "private_key_id": "553df3885d6c51eebac18a4c2b7d9169594b88f5",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCq279UpB4q00y6\n4GDELCscOOamCT2Bn1IFFFWMP97O/0BxELJ65HKDCPpH9NODpmbb7AS/etGIh1Xe\nBcNDSJg/r8Ta9I83rBiZfN3lRJmta2LFKb30poyuHxEullnCzf/7WbEqY6dv9HWQ\n95hj2Xr1Q0XkRpnqDNRGKkLPt/uKTxLof+uH6oky1vgc7JUZH+YZNo7DivJT5klm\nn8oQfLIK1mKJe2BCeYl5suKI/jQqt/XCc1ZePgPFBGQ78EYocspEsG0NML4bGJHs\nS+vBKGNDYn2kap3ktET8nwhabiB8paynNYFLw1R5W3iAsNxQgL3SSdm9PepjYWmZ\nYsKpfkCDAgMBAAECggEAEEzzxZL8z9Al72RNxxmBqWkiVC/ofs/g5twoRz+mta/z\niXXy2TenVyoJmsjYTySWhp/PWidRC0oCHrMFDIvF/rl5ufwAF+si063ui5uOX9Wx\ncCcJ2Of03v3WyU+N08CMjgHiHa2xQUSc3M5KayhKC1E2P0+fCo3byK/qfN/ML0cw\nvzKdB7kYHpSk2KNnIDa20mCl9QnTutT5MVD3thmi+pPBWb9IUWPX1FNpW72KgpDN\nN78jivn5fz20zFKCrtMiILrX+T5N+35yFpIcucvZ67wE/TrCH8hcdK35b9dk9ffZ\n1vAbSj+S2OAgrOfdFVQbYqHfp/qypQHU0jmhS36hzQKBgQDu9m8yMvXOZZezuXWC\nKYOle3GlntGFCCAT7r9Zci+aGsweaRPXHF4exEm1ZarY2ExCOxTCK1qpF1FDk1O+\nZdP1miP0tFoEcPqysy4OTG3CMYH+KFRDpt1/7wMFYGo3KwdWQCDT3N9esxtT6SEN\ntzxrRwUXdgcfjc3K2I006vGuZQKBgQC3CkTLfz7ikkHPAxgYLAd7eA+zdW7bjPf5\njk6otVaRl8bLQsqoV0DZzV+bwu2PhU0F3UumrhtytB6aXMVuypdr/9sdTilcV37S\nttNq28ftTag2OfQG+yRzU/lRP3ZrGGMUWUj0AWRv7opE76Z9gII4bsLfuQCZLocT\n87qnJQ3wxwKBgBnmLbEUIt4G1sVM4XaFB1alJXEc4Hp5ofhnFOgd3xjltJ/LJbJX\nyb+t6Is3hKfR8ZnwC1TsG/xdoZogWqA1Kx7gYOtBrMv0bsd1chVspSy57uvb9R4L\n9M/L2Nj5VSm7iSUI+EXeF3uND/YtOz7gUDUUUnHzgdwio15L0CofGKidAoGBALNx\nXLpHd+X1TpDczq071OYFcRcVJGYW0DAWhCS/CixXqGsygq0ARTKBNZ7lPbH7E+SQ\n645vl7cev/XCx0dzU3lsbmpPaxr9J/b5h1B2QIzzGdp3fDWv1i89/ujZF4Wsdc3I\nLk4QY1+ccm9cplLZPlCGvYNIwj5qL8Cuq6kbGYyXAoGBALDJSvkdKbtWMhT6BDc2\n4BFkLh6k/qnLN/zmV1WVq5yrOS9fzE50N4ApaDhKZQsthAx6rycDmAp8faxpGwwC\n3RT5kyqOzDpL4xznw+hqx2qCOfDYc58C0yDKCjXWyKg4pMRWWD/5qpYfxvCAZiFa\nJC1Q5XdSC3tp4k3E1ZZqpE3y\n-----END PRIVATE KEY-----\n",
  "client_email": "owner-739@trademaster5000.iam.gserviceaccount.com",
  "client_id": "106860157769563890726",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/owner-739%40trademaster5000.iam.gserviceaccount.com"
}


credentials = ServiceAccountCredentials.from_json_keyfile_dict(
         creds, scope) # Your json file here

gc = gspread.authorize(credentials)

wks = gc.open("Positions").sheet1

data2 = wks.get_all_values()
headers = data2.pop(0)

df = pd.DataFrame(data2, columns=headers)
df.head()
positions=df.to_dict('records')


# In[12]:


# stable_positions=json.load(open('stable_positions.json'))
# if len(positions)>len(stable_positions):
#     for i in range(len(stable_positions),len(positions)):
#         stable_positions.append(positions[i])
# positions=stable_positions
# with open('stable_positions.json', 'w') as fp:
#     json.dump(positions, fp, cls=JSONEncoder)


# In[13]:


data_url = 'https://datahub.io/core/s-and-p-500-companies/datapackage.json'
package = datapackage.Package(data_url)
resources = package.resources
for resource in resources:
    if resource.tabular:
        data = pd.read_csv(resource.descriptor['path'])
#         print (data)

dict_of_df={}
for i in range(0,len(data['Symbol'])):
    key_name=str(data['Name'][i])
    dict_of_df[key_name]=yf.Ticker(data['Symbol'][i]).history(period='180d', interval="1h")
    dict_of_df[key_name]['datetime']=pd.to_datetime(dict_of_df[key_name].index)
    if i%50==0:
        print(i,(i/len(data['Symbol']))*100,'%')

name=[]
std=[]
for i in range(0,len(data['Symbol'])):
        key_name=str(data['Name'][i])
        name.append(key_name)
        comp=dict_of_df[key_name]['Close']
        std.append(comp.std())
df=pd.DataFrame(list(zip(name,std)))
df=df.sort_values(by=[1], ascending=False)
df=df.reset_index(drop=True)

comps=df
# comps=df
comps.columns=['comp','std']
# comps=comps.drop(5)
# comp.reset_index(drop=True)
lent=60
std_mult=0.33
stop_loss=0.05
training=7# comps.head(10)

for pos in positions:
    if pos['ticker'].upper() in data['Symbol'].unique():
        index = data['Symbol'].tolist().index(pos['ticker'])
        pos['comp']=data['Name'][index]        


# In[14]:


def buys(lent, std_mult, stop_loss, p,d,q):
    temp=[]
    price_temp=[]
    comp_temp=[]
    for comp in comps['comp']:
#         print(comp)
        prices=dict_of_df[comp]['Close']
        count=0
        for pos in positions:
            if str(pos['status']).lower=='open' and pos['comp']==comp:
                count=count+1
        if count<1:
            if len(prices)>0:
                today=prices[-1]
                prices=prices[len(prices)-lent:]
                std=prices.std()
                avg=prices.mean()
                model = ARIMA(prices, order=(p,d,q)).fit()
        #                     print(p,d,q)
                forecast = float(model.forecast())
        #         print(forecast)
                if today >=avg+(std*std_mult) and forecast>=today:
                    temp.append('Buy '+str(comp)+'. Forecast is '+ str(round(forecast,2))+' - Current price is '+str(round(today,2))+os.linesep)
                    comp_temp.append(comp)
                    price_temp.append(forecast-today)
                if today <=avg+(std*std_mult) and forecast>=today:
                    temp.append('Buy '+str(comp)+'. Forecast is '+ str(round(forecast,2))+' - Current price is '+str(round(today,2))+os.linesep)
                    comp_temp.append(comp)
                    price_temp.append(forecast-today)
    return temp, comp_temp, price_temp
            


# In[15]:


def closes(stop_loss):
    open_temp='Open Positions are:'
    temp=[]
    for pos in positions:
#         print(pos['status'].lower())
        if pos['status'].lower()=='open':
            comp=pos['comp']
            prices=dict_of_df[comp]['Close']
            today=prices[-1]
            model = ARIMA(prices, order=(p,d,q)).fit()
        #                     print(p,d,q)
            forecast = float(model.forecast())
            open_temp=open_temp+str(comp)+", "
#             print(today)
            if today>=float(pos['max_']):
                pos['max_']=today
            elif today<=float(pos['max_'])*(1-stop_loss):
                temp.append('Sell '+str(comp)+'. Bought price is '+str(pos['buy']))
            elif forecast<today:
                temp.append('Sell '+str(comp)+'. Bought price is '+str(pos['buy']))
            
    return temp, open_temp
#         if today<=max_*(1-stop_loss):
#             temp.append('Sell '+)


# In[16]:


lent=14
std_mult=0.888888
stop_loss=0.05
# training=7
p=1
d=2
q=2
min_prof=3

calls, comp_temp, price_temp=buys(lent, std_mult, stop_loss, p,d,q)
sells, opens=closes(stop_loss)
df=pd.DataFrame([calls,price_temp,comp_temp]).transpose()
df2=df.sort_values(by=1, ascending=False)
df2 = df2.reset_index(drop=True)
# df2.head()
temp_=[]
for i in range(0,len(df2[0])):
    if df2[1][i]>min_prof:
        temp_.append(df2[0][i])
calls=temp_
msg_1=os.linesep.join(calls)
msg_2=os.linesep.join(sells)
msg= msg_1+"  "+msg_2+os.linesep+opens


# In[19]:


from twilio.rest import Client


twilio_sid = 'AC181a030b0019bd4282845677340cfff3'
auth_token = '9ea76feaf587d0d335618a043ecbbf65'

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(twilio_sid, auth_token)

# this is the Twilio sandbox testing number
# from_whatsapp_number='whatsapp:+14155238886'
from_whatsapp_number='+14142402551'
# replace this number with your own WhatsApp Messaging number
# to_whatsapp_number=['whatsapp:+6585890169','whatsapp:+353876191931', 'whatsapp:+353857531373']
to_whatsapp_number=['+353857531373']
# to_whatsapp_number=['whatsapp:+6585890169']

for i in to_whatsapp_number:
#     print(i)
    message=client.messages.create(body=msg,
                           from_=from_whatsapp_number,
                           to=i)
    print(message)
# i=to_whatsapp_number[0]
# message=client.messages.create(body=msg,
#                            from_=from_whatsapp_number,
#                            to=i)
# print(message)


# In[20]:


print(msg)


# In[ ]:




