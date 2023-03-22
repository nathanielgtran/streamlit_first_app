import streamlit as st
import pandas as pd

st.title('Our first Streamlit App')
st.subheader('intro to streamlit and automate everything with python')

data = {
  'Series_1':[1,2,4,5,9],
  'Series_2':[11,22,66,144,255,]
}

df = pd.DataFrame(data)



st.write(''' this us our first web app

wow very nice!
:D

\n( •_•)
\n( •_•)
\n( •_•)
\n( •_•)



''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celisus')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)