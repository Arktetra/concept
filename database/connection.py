# First run 'pip install mysql-connector-python psycopg2'

import sqlite3

def connect_to_db(concept.db):
    connection = sqlite3.connect(concept.db)
    return connection

