import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import matplotlib.dates as mdates
import pandas as pd

def plot_stock_trend(df):
    plt.figure(figsize=(10,10))

    df['date'] = pd.to_datetime(df['date'])  # Ensure 'date' is in datetime format

    # Plot the data
    plt.plot(df['date'], df['close'], label='Closing Price')

    # Set title and labels
    plt.title('Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')

    # Adjust x-axis ticks and formats
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())  # Automatic date locator
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format dates
    
     # Set appropriate x and y limits
    plt.xlim(min(df['date']), max(df['date']))
    y_min, y_max = min(df['close']), max(df['close'])
    y_range = y_max - y_min
    plt.ylim(y_min - y_range * 0.05, y_max + y_range * 0.05)  # Add some padding to y-axis
    
    # Set y-axis ticks
    y_ticks_interval = round(y_range / 10, 2)  # Divide the range into 10 parts
    y_ticks = np.arange(y_min, y_max + y_ticks_interval, y_ticks_interval)
    plt.yticks(y_ticks)

    # Add legend and layout adjustments
    plt.legend()
    plt.tight_layout()

    st.pyplot(plt)

    