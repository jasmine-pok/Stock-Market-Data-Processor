# Script to fetch stock data from Alpha Vantage

import requests
import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3

# Load environment variables
# load_dotenv()

def fetch_stock_data(symbol, start_date, end_date):
    """
    # Retrieve API key from .env
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    """
    api_key = st.secrets["alpha_vantage"]["api_key"]
    if not api_key:
        raise ValueError('API key not found')
    
    # Define the API endpoint and parameters
    url = f'https://www.alphavantage.co/query'
    params = {
        'function' : 'TIME_SERIES_DAILY',
        'symbol' : symbol,
        'apikey' : api_key,
        'datatype' : 'json',
    }

    # Make a GET request to the API endpoint
    response = requests.get(url, params=params)

    """ Debugging: print raw response
    print("Raw API Response:")
    print(response.json())
    """

    if response.status_code != 200:
        raise ValueError(f"Error fetching data: {response.status_code}, {response.text}")
    
    data = response.json()

    # Transform the data into a Pandas DataFrame
    if 'Time Series (Daily)' not in data or not data['Time Series (Daily)']:
        raise ValueError("No data found in API response. Check the symbol or try again later.")    
    
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.rename(columns={
        '1. open' : 'open',
        '2. high' : 'high',
        '3. low' : 'low',
        '4. close' : 'close',
        '5. volume' : 'volume'
    })
    # copies the index (dates) to a new column 'date'
    df['date'] = pd.to_datetime(df.index)
    # rearranges the columns to include only relevant fields 
    df = df[['date', 'open', 'close', 'high', 'low', 'volume']]

    # convert relevant columns to numeric
    numeric_columns = ['open', 'high', 'low', 'close', 'volume']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # add the stock symbol as a new column
    df['symbol'] = symbol

    """ Debugging: print raw data
    print("Raw Dataframe:")
    print(df.head())

    # Debugging: print the date range in the raw data 
    print(f"Data range in raw data: {df['date'].min()} to {df['date'].max()}")
    """

    # Convert start_date and end_date to datetime (in case they are strings)
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    """Debugging: Print the date range you're filtering with
    print(f"Filtering between {start_date} and {end_date}")
    """

    # Filters the DataFrame to include only the data within the specified date range
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]   # Filter the data by date range
    
    """ Debugging: print filtered data
    print("Filtered Dataframe:")
    print(df.head())


    # Debugging: Check the filtered data range
    if not df.empty:
        print(f"Data range after filtering: {df['date'].min()} to {df['date'].max()}")
    else:
        print("No data available for the selected date range.")

    print(f"Dataframe size after filtering: {df.shape}")
    """
    
    df = df.sort_values(by='date')

    return df

def save_data_to_db(df):
    # Connect to the SQLite database
    db_path = 'database.stock_data.db'
    conn = sqlite3.connect(db_path)

    # Insert the data into the database
    df.to_sql('stocks', conn, if_exists='replace', index=False)

    conn.close()
