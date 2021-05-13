# Data Science Project Spring 2021

## Investment Robot Counsellor

### Group

- Sofie Amalie Landt - cph-sl307@cphbusiness.dk
- Amanda Juhl Hansen - cph-ah433@cphbusiness.dk
- Benjamin Aizen Kongshaug - cph-bk131@cphbusiness.dk

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

### 2. Integrate the sources in shared repository by either ETL or ELT process (you can use public software, own code, or integration of tools)

The data is integrated into [this file](https://github.com/kongshaug/DS_big_project/blob/main/Stage_2.ipynb)

### 3. Design a Data Story or Data Processing Scenario 

Have a look at our [data story](https://github.com/kongshaug/DS_big_project/blob/main/DataStory.pdf)

## Stage 3: Integrating AI

### 1. Select relevant Machine Learning methods and development tools

We have used a LSTM model and a Regression model to explore the better fit for our project.

### 2. Create the AI module

We have decided to train the two models with data from only two stocks, to demonstrate which of the models to choose. The saved LSTM model have been trained with data from about 500 stocks. 

[This link](https://github.com/kongshaug/DS_big_project/blob/main/tactic-20210513T141746Z-001/tactic/lstm.ipynb) shows the training of both LSTM model and Regression model. Furthermore the implementation of the saved LSTM Model version 6.

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
