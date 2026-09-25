import streamlit as st
import joblib
import pandas as pd
import numpy as np


st.set_page_config(page_title="Housing Price Predictor", layout="wide")


model = joblib.load('./models/ridge.pkl')
model_columns = model.feature_names_in_


st.sidebar.header("Property Features")


surface_area = st.sidebar.slider("Living Area (Square Feet)", min_value=500, max_value=5000, value=1500, step=50)

st.sidebar.subheader("Location Details")
stonebr = st.sidebar.selectbox("Neighborhood: Stone Brook", ["No", "Yes"])
noridge = st.sidebar.selectbox("Neighborhood: Northridge", ["No", "Yes"])
mitchel = st.sidebar.selectbox("Neighborhood: Mitchell", ["No", "Yes"])
landslope = st.sidebar.selectbox("Severe Land Slope", ["No", "Yes"])

st.sidebar.subheader("Quality & Utilities")
kitchen = st.sidebar.selectbox("Excellent Kitchen Quality", ["No", "Yes"])
bsmt_qual = st.sidebar.selectbox("Excellent Basement Quality", ["No", "Yes"])
bsmt_exp = st.sidebar.selectbox("Good Basement Exposure", ["No", "Yes"])
roof = st.sidebar.selectbox("Wood Shingle Roof", ["No", "Yes"])
functional = st.sidebar.selectbox("Typical Home Functionality", ["No", "Yes"])
saletype = st.sidebar.selectbox("New Construction Sale", ["No", "Yes"])

st.sidebar.divider()

predict_btn = st.sidebar.button("Predict Price", type="primary", use_container_width=True)


st.title("🏠 Housing Price Predictor")
st.caption("Ames Housing Dataset — Ridge Regression model trained on LogSalePrice")
