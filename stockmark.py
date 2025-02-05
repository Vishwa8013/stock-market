import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go


START = '2020-01-01'
TODAY = date.today().strftime('%Y-%m-%d')

st.title("STOCK MARKET PREDICITION WEBSITE  \n  BY : Vishwa , Mounish ,Vaishanavi,Pavithra ")
print("                 enter the slock name           ")

stocks = ("AAPL","TATACHEM.NS","GC=F","BTC=F","MSFT")
selected_stocks=st.selectbox("Select the stock for prediction",stocks)

n_years=st.slider("select the year to predicition",1,5)
period = n_years*365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data 

data_load_state = st.text("Load data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data ............done here it is !")

st.subheader('Raw date')
st.write(data.tail())

