from utils.fetch_data import fetch_stock_data
from utils.visualize_data import plot_stock_trend

if __name__ == '__main__':
    # Fetch data
    symbol = 'AAPL'
    start_date = '2021-01-01'
    end_date = '2021-12-31'

    # Fetch stock data
    df = fetch_stock_data(symbol, start_date, end_date)
    
    # Plot stock trend
    plot_stock_trend(df)
    
    print('Data successfully fetched and visualized')