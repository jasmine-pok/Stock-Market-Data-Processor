# Stock Market Data Processor

A stock market data processing tool built with Python and Streamlit that allows users to fetch historical stock data from Alpha Vantage, store it in a SQLite database, and visualize stock trends with interactive charts.

You can try the live version of the app here: [Stock Market Data Processor](https://sjpok-market-visualizer.streamlit.app/).

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Unit Tests](#unit-tests)
- [Files and Modules](#files-and-modules)
- [Dependencies](#dependencies)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)

## Features

- Fetches stock data for a given symbol and date range from the [Alpha Vantage API](https://www.alphavantage.co/).
- Stores the fetched stock data in a SQLite database.
- Visualizes stock trends with a line chart for closing prices using [Matplotlib](https://matplotlib.org/).
- Simple user interface built with [Streamlit](https://streamlit.io/).

## Tech Stack

This project utilizes the following technologies and tools:

- **Python**: The core programming language used for backend logic and data processing.
- **Streamlit**: A Python framework used for building interactive web applications to visualize stock data and trends.
- **Alpha Vantage API**: Provides stock market data through its API for fetching historical stock information.
- **Pandas**: A powerful data manipulation library used to clean, filter, and process stock data.
- **SQLite**: A lightweight database used for storing the stock data locally in the `stock_data.db` file.
- **Matplotlib**: A plotting library used for visualizing stock price trends via line charts.
- **pytest**: A testing framework used to ensure the functionality of the application.
- **dotenv**: A Python package for managing environment variables securely (used for storing API keys).

## Project Structure
```plaintext
Stock-Market-Data-Processor/
│
├── app.py                        # Streamlit app for data fetching and visualization
├── requirements.txt              # List of project dependencies
├── LICENSE                       # Project license
├── README.md                     # Project documentation
├── .gitignore                    # Git ignore file
├── database/
│   ├── init_db.py                # Initialize the database
│   └── stock_data.db             # SQLite database to store stock data
│
├── data/                         # (Optional) Directory for storing fetched stock data
│
├── tests/                        # Directory for unit tests
│   ├── __init__.py               # Initialize the tests module
│   ├── test_fetch_and_store.py   # Unit test for fetch_data.py and database storage
│   └── test_visualization.py     # Unit test for visualize_data.py and charts
│
├── utils/                        # Utility scripts
│   ├── fetch_data.py             # Fetches stock data from Alpha Vantage
│   └── visualize_data.py         # Visualizes stock price trends
│
└── venv/                         # Virtual environment (created during setup)
```

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/jasmine-pok/Stock-Market-Data-Processor.git
   cd Stock-Market-Data-Processor
   
2. Set up a virtual environment (if you don't have one already)
   ```bash
   python3 -m venv venv
   
3. Activate the virtual environments
   - For Windows:
     ```bash
     venv\Scrips\activate
   - For macOS/Linux:
     ```
     source venv/bin/activate
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

5. Set up your Alpha Vantage API key:
   - Go to [Alpha Vantage](https://www.alphavantage.co/) to get an API key.
   - Add the API key to the environment variables:
     - You can set it in a .env file or use Streamlit secrets for secure key management.
    
## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
2. Open the app in your web browser (usually at http://localhost:8501).
3. Enter a stock symbol (e.g., AAPL for Apple) and select a date range. Click Fetch Data to retrieve the stock data.
4. The fetched data will be displayed in a table, and a line chart of the closing prices will be shown.
5. The stock data will be stored in the database.stock_data.db SQLite database for future use.

## Unit Tests

This project includes unit tests to ensure the functionality of the data fetching and visualization modules. To run the tests, ensure you have installed the dependencies as listed above.

Run the tests using pytest:
```bash
pytest tests/
```

## Files and Modules

- **`fetch_data.py`**: Fetches stock data from Alpha Vantage and stores it in a SQLite database.
- **`visualize_data.py`**: Generates a line chart to visualize the stock price trend.
- **`app.py`**: The main Streamlit app for interacting with the stock data.
- **`init_db.py`**: Initializes the SQLite database (if needed).
- **`test_fetch_and_store.py`**: Unit tests for fetching and storing stock data.
- **`test_visualization.py`**: Unit tests for stock data visualization.

  ## Dependencies

- `requests` - For making HTTP requests to the Alpha Vantage API.
- `pandas` - For data manipulation and handling.
- `matplotlib` - For plotting the stock price trends.
- `streamlit` - For building the web interface.
- `python-dotenv` (optional) - For managing environment variables.
- `pytest` - For running tests.

Install all dependencies via:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Alpha Vantage](https://www.alphavantage.co/) for providing the stock data API.
- [Streamlit](https://streamlit.io/) for creating the easy-to-use app interface.
- [Matplotlib](https://matplotlib.org/) for the powerful data visualization capabilities.

## Authors
  For any questions or feedback, feel free to contact us at:
- **Socheata (Jasmine) Pok** - [socheatajpok@gmail.com](mailto:socheatajpok@gmail.com)


