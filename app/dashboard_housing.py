import streamlit as st
import joblib
import pandas as pd
import numpy as np


st.set_page_config(page_title="Housing Price Predictor", layout="wide")


model = joblib.load('./models/ridge.pkl')
model_columns = model.feature_names_in_

