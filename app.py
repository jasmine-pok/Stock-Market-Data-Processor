import streamlit as st
from utils.fetch_data import fetch_stock_data, save_data_to_db
from utils.visualize_data import plot_stock_trend   
import pandas as pd

# Streamlit UI
st.title("Stock Market Data Processor")
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
start_date = st.date_input("Enter Start Date (YYYY-MM-DD):", pd.to_datetime("2024-09-03"))
end_date = st.date_input("Enter End Date (YYYY-MM-DD):", pd.to_datetime("2025-01-27"))
fetch_button = st.button("Fetch Data")

if fetch_button:
    try:
        # Fetch stock data
        df = fetch_stock_data(symbol, start_date, end_date)

        if df.empty:
            st.warning("No data found for the given symbol and date range. Please try different inputs.")
        else:
            # Save data to the database
            save_data_to_db(df)
            st.write("Fetched Data", df)
            
            # Plot stock trend
            plot_stock_trend(df)
    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")



