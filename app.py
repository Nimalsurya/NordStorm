import streamlit as st
import pandas as pd
#from sklearn.preprocessing import StandardScaler
import pickle
st.title('Reviews Prediction App ⭐')

#step 1
model = open('rfc.pickle','rb')
clf = pickle.load(model)
model.close()

#step2 : Creating Widgets

category = st.number_input('CATEGORY',1,6,step = 1)
subcategory = st.slider('SUBCATEGORY', 0,80,0)
productname = st.slider('PRODUCT_NAME',0,114073,0)
brand = st.slider('BRAND',0,2028,0)
pricecurrent = st.slider('PRICE_CURRENT',-4.7,2.73,-4.7)
reviewcount = st.slider('REVIEW_COUNT',-0.7,2.0,-0.7)
promotionlevel = st.slider('Promotion Level',0,7,0)
#age = st.slider('Age',21,81,21)

#step 3 : converting user input into model input

data = {'CATEGORY' : category,
        'SUBCATEGORY' : subcategory,
        'PRODUCT_NAME' : productname,
        'BRAND' : brand,
        'PRICE_CURRENT' : pricecurrent,
       'REVIEW_COUNT' : reviewcount,
        'Promotion Level' : promotionlevel }
input_data = pd.DataFrame([data])

#step4 : Get Predictions
preds = clf.predict(input_data)[0]
if st.button('Predict'):
    if preds == 1:
        st.success('The Predicted Rating is Good ⭐⭐⭐⭐⭐ ')
    if preds == 0:
        st.success('The Predicted Rating is Average ⭐⭐⭐')
    if preds == 2:
        st.error('The Predicted Rating is Poor 🫣')
