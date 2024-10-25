import streamlit as st
import joblib as jb 
import tensorflow as tf

model = tf.keras.models.load_model("model_churn.h5")
st.title('Bank Customer Churn Prediction')

v1 = st.number_input("Credit_Score (350-900)")
v2 = st.number_input("Age (above 18)")
v3 = st.number_input("Tenure (0-10)")
v4 = st.number_input("Balance (1k to 500k)")
v5 = st.number_input("NumOfProducts (1-5)")
v6 = st.number_input("HasCrCard (0-1)")
v7 = st.number_input("IsActiveMember (0-1)")
v8 = st.number_input("EstimatedSalary (1k to 200k)")
v9 = st.number_input("Geography_Germany (0-1)")
v10 = st.number_input("Geography_Spain (0-1)")
v11 = st.number_input("Gender (0-1) 0 for F , 1 for M")

# Define a function to make predictions
def make_prediction():
    input_data = [[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]]
    prediction = model.predict(input_data)
    return prediction

# Use the st.button with on_click parameter
if st.button('Submit'):
    prediction_result = make_prediction()
    # st.write("Prediction:", prediction_result)
    print(prediction_result)
    if prediction_result==1:
        st.write(" will churn")
    else:
        st.write("won't churn ")