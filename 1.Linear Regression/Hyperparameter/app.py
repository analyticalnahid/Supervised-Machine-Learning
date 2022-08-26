#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
import streamlit as st
import pickle


# In[49]:


## loading the model
pickle_in = open('pipe.pkl', 'rb')
regressor = pickle.load(pickle_in)

param_lst = ['OverallQual', 'YearBuilt', 'YearRemodAdd', 'BsmtFinSF1','TotalBsmtSF','1stFlrSF','GrLivArea','BsmtFullBath','FullBath','BedroomAbvGr','TotRmsAbvGrd','GarageYrBlt', 'GarageCars', 'GarageArea']


# In[50]:


def welcome():
    print("Welcome all")
    
def prediciton(param_lst):
    prediciton = regressor.predict([param_lst])
    print(prediciton)
    return prediciton

def nameit(name):
    name = st.text_input(name)

def main():
    st.title("House Price Prediction")
    
    nameit('OverallQual')
    nameit('YearBuilt')
    nameit('YearRemodAdd')
    nameit('BsmtFinSF1')
    nameit('TotalBsmtSF')
    nameit('1stFlrSF')
    nameit('GrLivArea')
    nameit('BsmtFullBath')
    nameit('FullBath')
    nameit('BedroomAbvGr')
    nameit('TotRmsAbvGrd')    
    nameit('GarageYrBlt')  
    nameit('GarageCars')  
    nameit('GarageArea')         
        
    result = ""
    if st.button("Predict"):
        result = prediciton(param_lst)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()


# In[ ]:




