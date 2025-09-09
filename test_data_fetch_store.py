import requests
import mysql.connector
import unittest
from config import DB_CONFIG

class TestDataFetchStore(unittest.TestCase):

    def setUp(self):
        # Connect to MySQL Database (test DB)
        self.conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        self.cursor = self.conn.cursor()
        
        # Create a sample table if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sample_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL
            )
        ''')
        # Clean previous test data
        self.cursor.execute('DELETE FROM sample_data')
        self.conn.commit()

    def test_fetch_and_store_data(self):
        # Step 1: Fetch data from sample API
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Step 2: Store fetched data into MySQL
        title = data['title']
        self.cursor.execute('INSERT INTO sample_data (title) VALUES (%s)', (title,))
        self.conn.commit()
        
        # Step 3: Verify data is stored correctly
        self.cursor.execute('SELECT title FROM sample_data')
        stored_title = self.cursor.fetchone()[0]
        
        self.assertEqual(stored_title, title)

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
