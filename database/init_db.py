import sqlite3

def create_db():
    # Connect to the SQLite database (create it if it doesn't exist)
    db_path = 'database.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Define the table schema
    c.execute('''CREATE TABLE IF NOT EXISTS stocks(
              date TEXT,
              symbol TEXT,
              open REAL,
              close REAL,
              high REAL,
              low REAL,
              volume INTEGER)''')
    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()


