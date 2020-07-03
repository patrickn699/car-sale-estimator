# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:10:52 2020

@author: Prathmesh
"""


import streamlit as st
import pickle
#from googleimagedownloader.googleimagedownloader import GoogleImageDownloader as gd
import base64
import pandas as pd
import webbrowser

pik = open('car_r.p', 'rb')
model = pickle.load(pik)


def get_table_download_link(df):
    
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    #return f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    #return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download csv file</a>' # decode b'abc' => abc
    return f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'





def main():
    
    menu = ['Prediction', 'About']
    sell = st.sidebar.selectbox('Select Option', menu)
    
    if sell == 'Prediction':
    
    
        st.title("Car Sale Price Estimator")
        
        print('')
        
       
            
        
        
        with open("style.css") as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
        st.image('head2.jpg')
        
    
        
            
        
        st.subheader('Enter the year in which you bought')
        
        
        yr = st.number_input('', key = 0)
        
        
        
        st.subheader('At what price did you purchased? (in lakhs)')
       
        present_pr = st.slider(' ',1,100)
        st.text(present_pr)
      
        
        st.subheader('Enter the kilometer driven')
        
        km = st.number_input('', key = 1)
        st.text(km)
        
        st.subheader('Is your car first hand, secod hand or third?')
        
        ow = st.number_input('', key = 2)
        st.text(ow)
        
        st.subheader('Select the fuel type ')
        typ = st.radio(' ', ('Petrol', 'Diesel','CNG'))
        st.text(typ)
        
        if typ =='Petrol':
            fuel_p = 1
            fuel_d = 0
        
        elif typ == 'Diesel':
            fuel_p = 0
            fuel_d = 1
            
        else:
            fuel_p = 0
            fuel_d = 0
            
        
        st.subheader('Select the type of transmission')
        trnas = st.selectbox(' ', ['Manaual', 'Automatic'])
        st.text(trnas)
        
        if trnas == 'Manaual':
            tr_m = 1
            
        else:
            tr_m = 0
        
        st.subheader('Are you a dealer or an individual?')
        sell = st.selectbox(' ', ['individual', 'dealer'])
        st.text(sell)
        
        if sell == 'individual':
            sell_i = 1
        
        else:
            sell_i = 0
        
        
        print('')
        print('')
        
        
        
        curr = 2020-yr
        #st.text(curr)
        
        pred = model.predict([[present_pr,km,ow,curr,fuel_d,fuel_p,sell_i,tr_m]])
        
        op = round(pred[0],2)
        
        if st.button('calculate estimated selling price',key=3):
            out = ('Estimated cost will be:'+" "+str(op))
            st.success(out)
        
        data = [present_pr,km,ow,yr,typ,sell,trnas,op]   
        df = pd.DataFrame([data], columns=['Present_Price', 'km driven', 'owner', 'year', 'feul_type','seller_type', 'transmission_type','est sale price'])
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)
        
        

    
    elif sell == 'About':
        
        url = 'https://github.com/patrickn699/car-sale-estimator.git'
        
        st.header('About this project.')
        st.write('')
        st.write('This project is about estimating or predicting the sale price of car.')
        st.write('The dataset used for the project is downloaded form kaggle.')
        st.write('I have built a machine learning model which is trained on this data.')
        st.write('It requires some dependencies before you can run on your local machine, so I am providing requirements.txt on my github page & also includes all the other files.  ')
        
        if st.button('github link'):
            webbrowser.open_new_tab(url)
    
    
if __name__ == '__main__':
    main()