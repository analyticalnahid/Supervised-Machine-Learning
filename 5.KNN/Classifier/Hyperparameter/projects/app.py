#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pnd  
import numpy as nmp  
import pickle as pkl  
import streamlit as smt
from PIL import Image as img  


# In[24]:


pickle_in = open('pipe.pkl', 'rb')
classifier = pkl.load(pickle_in)


# In[32]:


def welcome():  
    return 'welcome you all'  
    

def prediction(Gender,Age,EstimatedSalary):    
     
    prediction = classifier.predict(  
        [[Gender,Age,EstimatedSalary]])  
    print(prediction)  
    return prediction  
        
    
def main():  
 
    smt.title("Product Purchase Prediction")  
        
    html_temp = """  
    <div style = "background-colour: #FFFF00; padding: 16px">  
    <h1 style = "color: #000000; text-align: centre; "> Streamlit Iris Flower Classifier ML App   
     </h1>  
    </div>  
    """  
        
    smt.markdown(html_temp, unsafe_allow_html = True)  
    Gender = smt.selectbox("Gender", ['Male','Female'], index= 0)
    Age = smt.text_input("Age")
    EstimatedSalary = smt.text_input("Salary")
    result = " "  
    

    if smt.button("Predict"): 
        if prediction(Gender,Age,EstimatedSalary) == 0:
            smt.success('Will not Purchase')
        else:
            smt.success('Will Purchase')
            
    
    
if __name__== '__main__':  
    main()  


# In[ ]:





# In[ ]:





# In[ ]:




