 # Script to set up the database

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection
from lib.db.seed import seed_data

 
def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    with open("lib/db/schema.sql") as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)
        print("Database created :)")
        
        seed_data()
        print("Seeded database :)")
        
if __name__ == "__main__":
    setup_db()

    
    
    
"""
#from db import get_connection,seed_data

import sqlite3

conn = sqlite3.connect('articles.db')
cursor = conn.cursor()

 
def setup_db():
    with open("db/schema.sql") as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)
        print("Database created :)")
        
        # seed_data()
        # print("Seeded database :)")
        
        
if __name__ == "__main__":
    setup_db()

"""