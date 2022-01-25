import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title('House Price Predictor')

posted_by = st.selectbox('Posted by',['Dealer','Owner','Builder'])

under_construction = st.selectbox('Under Construction',['No','Yes'])

bhk_no = st.selectbox('BHK NO',[1,2,3,4,5])

square_ft = st.number_input('SQUARE_FT')

location = st.selectbox('Location', df['LOCATION'].unique())

if st.button('Predict Price'):
    
    if posted_by == 'Dealer':
        posted_by = 2
    elif posted_by == 'Owner':
        posted_by = 1
    else:
        posted_by = 0
    
    if under_construction == 'Yes':
        under_construction = 1
    else:
        under_construction = 0

    query = np.array([posted_by,under_construction,bhk_no,square_ft,location])

    query = query.reshape(1,5)
    st.title(int(pipe.predict(query)))