import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go


START =" 2024-01-01"
TODAY = date.today().strftime("%y-%m-%d")

st.title("STACK MARKET PREDICITION WEBSITE \n  BY : Vishwa , Mounish ,Vaishanavi Pavithra")

stocks = ( "select the slock name ","AAPL","GOOG","MSFT")
selected_stocks=st.selectbox("Select the stock for prediction",stocks)

n_years=st.slider("select the year to predicition",1,5)
period = n_years*365
