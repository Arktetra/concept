# First run 'pip install mysql-connector-python psycopg2'

import sqlite3
fd = open('schema.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')
connection = sqlite3.connect("concept.db")

def list_tables(connection):
    #See what tables are present in database
    cursor = connection.cursor()
    query = "SELECT name FROM sqlite_master WHERE type='table';" 
    cursor.execute(query)
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    cursor.close()


def view_table(connection, table_name):
    #View the table
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    
