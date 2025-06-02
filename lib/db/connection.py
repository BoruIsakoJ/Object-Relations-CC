# Database connection setup
import sqlite3

conn = sqlite3.connect('articles.db')
conn.row_factory = sqlite3.Row 

def get_connection():
    return conn