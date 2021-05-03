#!/usr/bin/env python
# coding: utf-8

# ### stage 2: Business Data Storytelling
# 

# In[1]:


import talib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from os import listdir


# In[59]:


path = r"./data/stocks/"
files = listdir(path)# many crypto 

for indx, file in enumerate(files[4:7]):
    print("nr. "+str(indx) +"/"+ str(len(files[:])))
    indx = 2
    dataset = pd.DataFrame()
    dataset = pd.read_csv(path + file)
    if len(dataset) < 800 and indx != 0:
      print("Dataset smaller then 800 skipping ...")
      continue
    dataset["Open"] = dataset["Open"].astype(float)
    dataset["High"] = dataset["High"].astype(float)
    dataset["Low"] = dataset["Low"].astype(float)
    dataset["Close"] = dataset["Close"].astype(float)
    dataset = dataset.reset_index()
    dataset = dataset[['Close', 'High', 'Low', 'Open']]
    # dataset = dataset[['Close']]
    dataset = dataset.dropna()
    plt.figure(figsize=(20, 10))
    plt.plot(dataset["Close"],color='g', label='close price')
    plt.show()


# In[78]:


dataset['RSI'] = talib.RSI(dataset['Close'].values, timeperiod=20)
dataset['30day MA'] = dataset['Close'].shift(1).rolling(window=30).mean()
dataset['140day MA'] = dataset['Close'].shift(1).rolling(window=140).mean()
dataset.dropna(inplace=True)


# In[79]:


dataset_sample = dataset[:700]
plt.figure(figsize=(20, 10))
plt.plot(dataset_sample["Close"],color='black', label='close price')
plt.plot(dataset_sample["140day MA"],color='b', label='140day MA')
plt.plot(dataset_sample["30day MA"],color='g', label='30day MA')
plt.legend()
plt.show()


# In[85]:


dataset["buy"] = np.where(((dataset["RSI"]< 40 )),1,0) # & (dataset["140day MA"]<dataset["Close"])
dataset["sell"] = np.where(((dataset["RSI"]> 70 ) | (dataset["140day MA"]>dataset["Close"])),1,0) 

#moving 
dataset["buy"] = np.where((dataset["140day MA"]<dataset["Close"]) & (dataset["30day MA"]<dataset["Close"] ),1,0)
dataset["sell"] = np.where((dataset["140day MA"]>dataset["Close"]) | (dataset["30day MA"]>dataset["Close"] ),1,0)


# In[86]:


dataset[dataset["buy"] != 0]


# In[87]:


dataset["buy"] = np.where((dataset["buy"] == 1) &
                                  (dataset["buy"].shift(1) == 0), 1, 0)

dataset["buy_spot"] = np.where(
  (dataset["buy"] == 1), dataset["Close"], 0)

dataset["sell"] = np.where((dataset['sell'] == 1) &
                                (dataset['sell'].shift(1) == 0), 1, 0)

dataset["sell_spot"] = np.where(
  (dataset["sell"] == 1), dataset["Close"], 0)


# In[88]:


dataset


# In[90]:


dataset_sample = dataset[:1000]
plt.figure(figsize=(20, 10))
plt.plot(dataset_sample["Close"],color='black', label='close price')
plt.plot(dataset_sample["30day MA"],color='g', label='30day MA')
plt.plot(dataset_sample["140day MA"],color='g', label='140day MA')
plt.scatter(dataset_sample.index,dataset_sample["buy_spot"],color='b', label='30day MA', marker="x",s=100)
plt.scatter(dataset_sample.index,dataset_sample["sell_spot"],color='r', label='30day MA', marker="x",s=80)
plt.legend()
plt.show()


# In[91]:


dataset['Tomorrows Returns'] = 0.
dataset['Tomorrows Returns'] = dataset['Close'] - dataset['Close'].shift(1)
dataset


# In[92]:


own = False
own_days = []
accumulated_market_return = 0
accumulated_stradegy_return = 0

for indx, row in dataset.iterrows():
    if row["buy_spot"] != 0:
        own = True
    if row["sell_spot"] != 0:
        own = False
    own_days.append(own)   
      
dataset["own"] = own_days


# In[93]:


dataset['Strategy Returns'] = 0.
dataset['Strategy Returns'] = np.where(
  dataset['own'] == True, dataset['Tomorrows Returns'], 0)
dataset['Cumulative Market Returns'] = np.cumsum(
  dataset['Tomorrows Returns'])
dataset['Cumulative Strategy Returns'] = np.cumsum(
  dataset['Strategy Returns'])
dataset["buy"] = np.where((dataset['own'] == True) &
                              (dataset['own'].shift(1) == False), 1, 0)


# In[94]:


dataset


# In[95]:


dataset_sample = dataset
plt.figure(figsize=(20, 10))
plt.plot(dataset_sample["Cumulative Market Returns"],color='black', label='market return')
plt.plot(dataset_sample["Cumulative Strategy Returns"],color='b', label='30day MA')
# plt.scatter(dataset_sample.index,dataset_sample["buy_spot"],color='b', label='30day MA', marker="x",s=80)
# plt.scatter(dataset_sample.index,dataset_sample["sell_spot"],color='r', label='30day MA', marker="x",s=80)
plt.legend()
plt.show()


# In[96]:


print("the total accumilated market return is: ", dataset["Cumulative Market Returns"].iloc[-1])
print("the total accumilated Strategy return is: ", dataset["Cumulative Strategy Returns"].iloc[-1])


# In[97]:


pip install jupyter-dash


# In[111]:


import glob
files = glob.glob(r"C:\Users\benja\OneDrive\Skrivebord\skole\DataScience\bigproject\DS_big_project\data\Stocks/*.txt")

files = [file.split("\\")[-1] for file in files]


# In[113]:


files = ['a.us.txt',
 'burl.us.txt',
 'buse.us.txt',
 'buz.us.txt',
 'bv.us.txt',
 'bval.us.txt',
 'bvn.us.txt',
 'bvsn.us.txt',
 'bvx.us.txt',
 'bvxv.us.txt',
 'bvxvw.us.txt',
 'bw.us.txt',
 'bwa.us.txt',
 'bwen.us.txt',
 'bwfg.us.txt',
 'bwg.us.txt',
 'bwina.us.txt',
 'bwinb.us.txt',
 'bwl-a.us.txt',
 'bwld.us.txt',
 'bwp.us.txt',
 'bwxt.us.txt',
 'bx.us.txt',
 'bxc.us.txt',
 'bxe.us.txt',
 'bxg.us.txt',
 'bxmt.us.txt',]


# In[120]:


import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load Data
df = px.data.tips()

# Load file names


# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H1("DashBoard"),
    dcc.Graph(id='graph'),
    html.Label([
        "Stock",
        dcc.Dropdown(
            id='stock-dropdown', clearable=False,
            value='aby.us', options=[
                {'label': c, 'value': c}
                for c in files
            ])
    ]),
])
# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    [Input("stock-dropdown", "value")]
)
def update_figure(colorscale):
    return px.line(
        dataset,  y="Close", 
        render_mode="webgl", title="Closing price each day"
    )
# Run app and display result inline in the notebook
app.run_server(mode='inline')


# In[116]:


dataset


# In[ ]:




