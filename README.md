# Data Fetch & Store Test

This project tests fetching data from a public API and storing it into MySQL.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create MySQL test database and user:
    ```sql
    CREATE DATABASE test_db;
    CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'test_password';
    GRANT ALL PRIVILEGES ON test_db.* TO 'test_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

3. Run the test:
    ```bash
    python test_data_fetch_store.py
    ```
