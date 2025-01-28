import pytest
import pandas as pd
from utils.visualize_data import plot_stock_trend

def test_plot_stock_trend():
    test_data = {
        "date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "close": [105, 110, 115]
    }
    df = pd.DataFrame(test_data)

    # Ensure no exceptions are raised during plotting
    try:
        plot_stock_trend(df)
    except Exception as e:
        pytest.fail(f"Visualization failed with exception: {e}")
