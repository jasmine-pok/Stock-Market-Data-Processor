from utils.fetch_data import fetch_stock_data, save_data_to_db

# Test the functions
if __name__ == '__main__':
    # Fetch data
    symbol = 'AAPL'
    start_date = '2021-01-01'
    end_date = '2021-12-31'

    # Fetch stock data
    df = fetch_stock_data(symbol, start_date, end_date)
    
    # Save data to the database
    save_data_to_db(df)
    
    print('Data successfully fetched and saved to the database')