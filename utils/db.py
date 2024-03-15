import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
conn_params = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

# SQL command to create a table
create_table_command = """
CREATE TABLE IF NOT EXISTS fund_data (
    id SERIAL PRIMARY KEY, 
    fund_name VARCHAR(255),
    serie VARCHAR(50),  # Note: This should match your INSERT INTO column name
    fund_type VARCHAR(255),
    daily_variation VARCHAR(10),
    thirty_day_variation VARCHAR(10),
    yearly_variation VARCHAR(10),
    quota_value VARCHAR(20),
    registry_date DATE DEFAULT CURRENT_DATE
);
"""

def create_table():
    conn = None
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        
        # Execute the SQL command
        cur.execute(create_table_command)
        
        # Commit the changes to the database
        conn.commit()
        
        # Close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('... Table created!')
            conn.close()

# Run the create_table function
# create_table()




# # Assuming 'data_tuple' does not include a date; PostgreSQL will automatically fill it
# data_tuple = ("FI Deuda Chile series A", "A", "Some Fund Type", "-0,02%", "0,69%", "4,09%", "$1.253,5248")

def insert_data(data_tuples):  # Renamed function to avoid conflict
    conn = None
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        
       # Prepare the SQL command
        insert_query = """
        INSERT INTO fund_data (fund_name, serie, fund_type, daily_variation, thirty_day_variation, yearly_variation, quota_value)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        # Adjust each tuple to match the expected structure
        adjusted_data_tuples = [t[:-1] for t in data_tuples]  # This removes the last element from each tuple
        
        # Execute the SQL command for each adjusted tuple
        for data_tuple in adjusted_data_tuples:
            cur.execute(insert_query, data_tuple)
        
        # Commit the changes to the database
        conn.commit()
        
        # Close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('... Query inserted!')
            conn.close()
            

# Run the insert_data function
# insert_data()

