import os
from typing import Text
from psycopg2 import pool
from dotenv import load_dotenv, main
import psycopg2
# Load .env file
load_dotenv()#this is a function from dotenv library
def create_connection_pool():
    # Get the connection string from the environment variable
    
    # Create a connection pool
    try: 
        connection_pool = pool.SimpleConnectionPool(1, 20, os.getenv('DATABASE_URL'))
        if connection_pool:
            print("Connection pool created successfully.")

        # Get a connection from the pool
        connection = connection_pool.getconn()
        if connection:
            print("Successfully received a connection from the connection pool.")

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Execute a simple query
            cursor.execute("SELECT * from jobs")
            database_list= cursor.fetchall()
            
            # Get column names from cursor.description
            column_names = [desc[0] for desc in cursor.description]
            print(column_names, "\nHERE WE PRINTED THE COLUMN NAMES")
            # Print the column names
            database_dicts= [dict(zip(column_names, row)) for row in database_list]
            print(database_dicts)
            # Close the cursor and connection
            cursor.close()
            connection_pool.putconn(connection)
            return database_dicts
    except Exception as e:
        print(f"Error creating connection pool: {e}")        
      

if __name__=='__main__':
    pool=create_connection_pool()
    if pool:
        # Get a connection from the pool
        connection = pool.getconn()
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT version()')
            db_version = cursor.fetchone()
            print('PostgreSQL database version:', db_version)
            cursor.close()
        finally:
            # Return the connection back to the pool
            pool.putconn(connection)
    