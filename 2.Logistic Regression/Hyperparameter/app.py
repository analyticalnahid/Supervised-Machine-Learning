#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pnd  
import numpy as nmp  
import pickle as pkl  
import streamlit as smt  
from PIL import Image as img  


# In[20]:


## loading the model
pickle_in = open('pipe.pkl', 'rb')
classifier = pkl.load(pickle_in)


# In[22]:


def welcome():  
    return 'welcome you all'  
    

def prediction(SepalLength,SepalWidth,PetalLength,PetalWidth):    
     
    prediction = classifier.predict(  
        [[SepalLength,SepalWidth,PetalLength,PetalWidth]])  
    print(prediction)  
    return prediction  
        
    
def main():  
 
    smt.title("Iris Flower Prediction")  
        
    html_temp = """  
    <div style = "background-colour: #FFFF00; padding: 16px">  
    <h1 style = "color: #000000; text-align: centre; "> Streamlit Iris Flower Classifier ML App   
     </h1>  
    </div>  
    """  
        
    smt.markdown(html_temp, unsafe_allow_html = True)  
   
    SepalLength = smt.text_input ("Sepal Length ")  
    SepalWidth = smt.text_input ("Sepal Width ")  
    PetalLength = smt.text_input ("Petal Length ",)  
    PetalWidth = smt.text_input ("Petal Width ")  
    result = " "  
        

    if smt.button("Predict"):  
        result = prediction(SepalLength,SepalWidth,PetalLength,PetalWidth)  
    smt.success ('The output of the above is {}'.format(result))  
if __name__== '__main__':  
    main()  


# In[ ]:




