import streamlit as st
import pandas as pd
import plotly.express as px

from data_loader import load_data
from analysis import merge_datasets, compute_correlations, yearly_oil_trend
from ml_model import train_model

st.set_page_config(page_title="Oil Intelligence Dashboard", layout="wide")

st.title("🌍 Geopolitical Oil Market Intelligence")

events, exports, prices, risk, sanctions = load_data()

df = merge_datasets(prices, risk)

# Sidebar
st.sidebar.header("Filters")

year = st.sidebar.slider("Select Year", 1990, 2024, 2010)

prices['year'] = prices['date'].dt.year

filtered = prices[prices['year'] == year]

# Oil price chart
st.subheader("📈 Brent Oil Price Trend")

fig = px.line(prices, x="date", y="brent_usd")

st.plotly_chart(fig, use_container_width=True)

# Yearly trend
trend = yearly_oil_trend(prices)

st.subheader("📊 Yearly Oil Price Trend")

fig2 = px.bar(trend, x="year", y="brent_usd")

st.plotly_chart(fig2)

# Export analysis
st.subheader("🚢 Iran Oil Export Destinations")

fig3 = px.bar(exports, x="destination", y="estimated_revenue_bn_usd")

st.plotly_chart(fig3)

# Correlation heatmap
st.subheader("🔬 Market Risk Correlation")

corr = compute_correlations(df)

fig4 = px.imshow(corr)

st.plotly_chart(fig4)

# ML prediction
st.subheader("🤖 Oil Price Prediction Model")

model, score = train_model(df)

st.write("Model Accuracy (R² Score):", score)
