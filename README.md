# Data Science Project Spring 2021

## Investment Robot Counsellor

### Group

- Sofie Amalie Landt - cph-sl307@cphbusiness.dk
- Amanda Juhl Hansen - cph-ah433@cphbusiness.dk
- Benjamin Aizen Kongshaug - cph-bk131@cphbusiness.dk

### Installation guide

1. Run this command from the root of project to install required libraries:

````
pip install -r /requirements.txt
````

2. Install TA-Lib by downloading it and pip installing it from here: [TA-lib repo](https://github.com/mrjbq7/ta-lib)

3. Open the project in jupyter 

4. Run the notebook lstm_and_regression_models in the folder Neural_networks

## Stage 1: Business Case Foundation

### Inspirational links

- https://towardsdatascience.com/predicting-stock-price-with-lstm-13af86a74944
- https://towardsdatascience.com/lstm-time-series-forecasting-predicting-stock-prices-using-an-lstm-model-6223e9644a2f
- https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

### Context and purpose

The purpose of this project is to develope a system for predicting the change in stock prices. This system is meant as a supplement to support or contradict the descision to invest in a given stock. We want to develope this system by analyzing the evolvement in the stock prices, which can indicate the overall direction of the stock price. This can be done by using Machine Learning or market analysis. We will experiment with different solutions, with the purpose of finding the best possible solution for this project.

### Questions

1. What will happen if we use previous changes in the stock prices to predict future stock price development?
2. What can we expect from the many possible analysis methods to predict stock prices and are they at any help at all or are the changes in stock prices random?
3. What is the different result from Machine Learning vs. market analysis?

### Hypotheses

#### Null Hypotheses

Changes in stock prices are random and it's not possible to analyze and predict the future stock price.

#### Alternative Hypotheses

It is possible to predict future stock prices by using neural networks and market analysis

### What is in the focus of your interest?

This project will be focused on developing a system which can predict stock prices and thereby a positive or negative development of a given stock in the future. Our most important goal for the system is to predict the direction of the change, and therefor not the exact price change.

### Why is it interesting?

If it's possible to contradict the null hypotheses this project is interesting for us, because it means that normal people without knowledge of the stock market has a possibility to make profit by using this program.

### Which outcome do you expect from your research?

We expect that the null hypotheses is correct and thereby that it's not possible to predict the future changes in stock prices.

### Who may be a user of the results?

If the null hypotheses is correct this project can be used to proof that it is not possible to predict the stock market, and thereby prevent people / companies spending a lot of time and resources witout profit.

If the null hypotheses is contradicted everyone can use this project to make personal profit.

## Stage 2: Business Data Storytelling

### 1. Searching Internet and other media, find relevant data sources that can be used in your experiment.

The data is stored in [this data folder](https://github.com/kongshaug/DS_big_project/tree/main/data)

The dataset originates from [kaggle](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)
It is one of the largest open source datasets with stock price data.
It has both stock data and ETF data, we only use the stock data

### 2. Integrate the sources in shared repository by either ETL or ELT process (you can use public software, own code, or integration of tools)

For a further explanation of how each analysis is implemented and data is engineered, look into [this notebook](https://github.com/kongshaug/DS_big_project/blob/main/Data_processing_and_visualisation.ipynb)

In the notebook we load two stocks and performs a RSI and Moving Average analysis on them. 
Then we explore the data in order to see if the new generated parameters, can widen our understandig of the data. We will do this by plotting the data in a graph, and use it for analysing when to buy and sell the stocks. If the outcome of these analysis is not useful, it indicates that we should use more complex methods for prediction or combine these analysis with other types of data engineering for use in AI models. 

### 3. Design a Data Story or Data Processing Scenario 

Have a look at our [data story](https://github.com/kongshaug/DS_big_project/blob/main/DataStory.pdf)

## Stage 3: Integrating AI

### 1. Select relevant Machine Learning methods and development tools

We have used a LSTM model and a Regression model to explore the better fit for our project.

### 2. Create the AI module

We have decided to train the two models with data from only one stock, to demonstrate which of the models to choose. The saved LSTM model have been trained with data from about 500 stocks. 

[This link](https://github.com/kongshaug/DS_big_project/blob/main/Neural_networks/lstm_and_regression_models.ipynb) shows the training of both LSTM model and Regression model. Furthermore the implementation of the saved LSTM Model. 

#### Data pipeline - [Link](https://github.com/kongshaug/DS_big_project/blob/main/datastory.png) to see the pipeline in a bigger format (click download)

![data pipeline](https://user-images.githubusercontent.com/47500265/120844534-d32e4a00-c56f-11eb-91e5-6d4190b2f220.png)

#### Methods and algorithms to prepare the data for prediction

In order to use our data for prediction we go through five steps. 

1) We exclude unmeaningful data and only use: Close, High, Low and Open.

2) We generate new parameters to enrich the data fed to the model by performing market analysis on the stock prices.

3) We remove NaN values to clean up the data.

4) We scale the data in order for the model not to apply any meaning to the stock price value, but only in procential fluctuation.

5) Finally we split the data into a training and test dataset with a 80/20 split.


#### Methods and algorithms for prediction 

##### LSTM model 

For the LSTM model we have obtained the best results using Adam as the optimizer, and mean_squared_error as the loss function. Futhermore we have used 18 epochs, with a batch-size of 126 per stock. We did this since the model stopped improving after the 17th epoch and our RAM size limited us to 126 in the batch size.

This model consists of four LSTM layers with a dropout 20 % between each layer, to avoid overfitting and at last a dense layer. 


##### Regression model 

For the Regression model we have obtained the best results using Adam as the optimizer, Relu as activation function and mean_absolute_error as the loss function. Futhermore we have used 30 epochs, with a batch-size of 126 per stock. We did this for the sane reason as the LSTM model.

This model consists of five dense layers. The first four layers uses Relu as activation function and the last layer uses linear as activation function. 


##### We have cleaned up the notebook after this example was written and therefore the printouts in the notebook does not match the once below but the training process remains the same.


#### Regression Model and LSTM Model both validated with the same test data

<p align="center" width="100%">

<img src="https://user-images.githubusercontent.com/47500265/118152338-da50b500-b414-11eb-9973-006fda0d6753.png" alt="Regression" title="Regression Model" width="49%"> 

<img src="https://user-images.githubusercontent.com/47500265/118145758-38c66500-b40e-11eb-84dc-4fc33238ac81.png" alt="LSTM" title="LSTM Model" width="49%"> 
   
</p>

- As seen on the two graphs above, the LSTM Model (right model) have a higher return than the Regression Model (left model).

- The LSTM Model have predicted that the stock price would increase the following day - 990 out of 2362 days. Only 495 days out of these 990 days, the price actually increased the following day. This gives a total of 50 % correct predictions and 50 % of false positive. The validation loss of the LSTM Model is around 0.06 %.

- The Regression Model have predicted that the stock price would increase the following day - 2118 out of 2362 days. Only 1038 days out of these 2118 days, the price actually increased the following day. This gives a total of 49 % correct predictions and 51 % of false positive. The validation loss of the Regression Model is around 0.6 %.

- LSTM Models takes into consideration the last 35 days when predicting the following day's closing price. Through this the model gets an understanding of previous fluctuation and therefore a greater fundament for prediction. 

Based on this and our observations we have decided to work with the LSTM Model.

#### LSTM Model validated with new data

<img src="https://user-images.githubusercontent.com/47500265/118149368-c5265700-b411-11eb-8a91-0c38d3d06283.png" alt="LSTM" title="LSTM Model"> 
                                                                             
As seen on the graph above the return of the LSTM Model is significantly higher than the market return thorughout the time period. This is an indicium that our model have obtained a concept of stock price movement on the market, that exceeds the market return of the stock it has been trained on. 

### 3. Store the trained model in a file for further implementation

The saved trained LSTM models are based on data from 500 stocks each of these with a minimum of 800 working days on the stock market.

[This folder](https://github.com/kongshaug/DS_big_project/tree/main/models/models) contains the LSTM models for further use. We are using the 6th version. In the previous versions we have tested with different parameters like epochs, number of neurons and time-window. 

## Stage 4: Immersive Analytics and Visualisation

### 1. Consider applying 3D visualisation and VR/AR/MR techniques

#### AR mobile app

We want to illustrate how to implement an AR solution for visualize our data. The reason for choosing AR is that everyone has a smart phone available that makes this solution widely accessible. The idea is that the user can print out a company logo and use our app to visualize the stock data of the company. It is also possible to compare stock data between mulitple companies simply by placing the logos next to eachother on a table.

Each graph shows the market return and the LSTM strategy return as well as markers for when to buy and sell in relation to the LSTM model. This way it is easier for the users to analyse the results based on the visualization. 

We have tried to visualise our AR solution in the pictures below.

##### Picture 1


<img src="https://user-images.githubusercontent.com/47500265/119221057-caf4fa00-baed-11eb-88a2-27bddf5d7cb1.jpeg" alt="3Dvisualisering" width="40%" height="35%" align="center"> 

##### Picture 2


<img src="https://user-images.githubusercontent.com/47500265/119221063-cf211780-baed-11eb-840b-8b4fb37d099d.png" alt="3Dvisualisering"  width="40%" height="35%" align="center"> 

##### Picture 3


<img src="https://user-images.githubusercontent.com/47500265/119221060-ccbebd80-baed-11eb-92b5-5b238da5413d.jpeg" alt="3Dvisualisering" width="40%" height="35%" align="center"> 

##### Picture 4


<img src="https://user-images.githubusercontent.com/47500265/119221064-d0524480-baed-11eb-9a7e-b9017a98784a.png" alt="3Dvisualisering" width="40%" height="35%" align="center"> 

#### 3D heatmap

Another way to analyse the data is to make a 3d heatmap that can be used to determine which stocks our LSTM model would be sufficient for prediction. By visualising the accumulated return of our LSTM model over time we get a better understanding of the generel performance instead of only looking at the end result. With this technique we can account for sudden outliers and optain a broader understanding of the performance on multple stocks at once.

This 3d heatmap is just to illustrate the concept and does not use our data.


<img src="https://user-images.githubusercontent.com/47500265/119221962-3e990600-baf2-11eb-92f1-22a374e4a1aa.png" alt="heatmap" width="40%" height="40%" align="center"> 

This visualisation could also be shown in our AR mobile app.


### 2. Benefits of applying better visualisation techniques for data analytics

When we analyze data in the typical 2D format, usually comprised of numbers listed in a spreadsheet or grouped in a pie chart, there’s a limit to how much information we can actually take away and use for making decisions. 

Therefore the benefits of 3D techniques are as follows:
- More complex data can be visualized in AR.
- Better comprehension of distances and outliers in a more natural interaction.
- Being able to immerse yourself into the data

