import os
import pytest
import pandas as pd
from utils.fetch_data import fetch_stock_data, save_data_to_db
import sqlite3

# Mock the .env file or ensure it exists
@pytest.fixture(scope="module")
def setup_env():
    os.environ['ALPHA_VANTAGE_API_KEY'] = 'test_key'

# Test fetching stock data
def test_fetch_stock_data(mocker, setup_env):
    mock_response = {
        "Time Series (Daily)": {
            "2023-01-01": {"1. open": "100", "2. high": "110", "3. low": "90", "4. close": "105", "5. volume": "1000"},
            "2023-01-02": {"1. open": "105", "2. high": "115", "3. low": "95", "4. close": "110", "5. volume": "1500"},
        }
    }

    # Mock the requests.get method
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    df = fetch_stock_data("AAPL", "2023-01-01", "2023-01-02")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'date' in df.columns

# Test saving data to database
def test_save_data_to_db():
    test_data = {
        "date": ["2023-01-01", "2023-01-02"],
        "open": [100, 105],
        "close": [105, 110],
        "high": [110, 115],
        "low": [90, 95],
        "volume": [1000, 1500],
        "symbol": ["AAPL", "AAPL"]
    }
    df = pd.DataFrame(test_data)

    save_data_to_db(df)

    # Verify the data was saved
    db_path = 'database.stock_data.db'
    conn = sqlite3.connect(db_path)
    saved_data = pd.read_sql_query("SELECT * FROM stocks", conn)
    conn.close()

    assert not saved_data.empty
    assert len(saved_data) == 2
    assert all(saved_data['symbol'] == "AAPL")
