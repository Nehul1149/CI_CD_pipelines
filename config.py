# DB_CONFIG = {
#     "host": "localhost",
#     "user": "root",
#     "password": "@nehul114911#",
#     "database": "test_db"
# }

import os

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "@nehul114911#"),
    "database": os.getenv("MYSQL_DATABASE", "test_db")
}
