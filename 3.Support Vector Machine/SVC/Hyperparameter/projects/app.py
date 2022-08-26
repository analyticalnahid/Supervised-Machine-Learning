#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pnd  
import numpy as nmp  
import pickle as pkl  
import streamlit as smt  
from PIL import Image as img  


# In[5]:


## loading the model
pickle_in = open('pipe.pkl', 'rb')
classifier = pkl.load(pickle_in)


# In[6]:


def welcome():  
    return 'welcome you all'  
    

def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):    
     
    prediction = classifier.predict(  
        [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])  
    print(prediction)  
    return prediction  
        
    
def main():  
 
    smt.title("Heart Disease Prediction")  
        
    html_temp = """  
    <div style = "background-colour: #FFFF00; padding: 16px">  
    <h1 style = "color: #000000; text-align: centre; "> Streamlit Iris Flower Classifier ML App   
     </h1>  
    </div>  
    """  
        
    smt.markdown(html_temp, unsafe_allow_html = True)  
    age = smt.text_input("age ")
    sex = smt.text_input("sex ")
    cp = smt.text_input("cp ")
    trestbps = smt.text_input(" trestbps ")
    chol = smt.text_input("chol ")
    fbs = smt.text_input("fbs ")
    restecg = smt.text_input("restecg ")
    thalach = smt.text_input("thalach ")
    exang = smt.text_input("exang ")
    oldpeak = smt.text_input("oldpeak ")
    slope = smt.text_input("slope ")
    ca = smt.text_input("ca ")
    thal = smt.text_input("thal ")
    result = " "  
        

    if smt.button("Predict"):  
        result = prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)  
    smt.success ('The output of the above is {}'.format(result))  
    
    
if __name__== '__main__':  
    main()  


# In[ ]:




