from flask import Flask, request, jsonify
import pandas as pd
import pyodbc
from flask_cors import CORS
from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
app = Flask(__name__)
CORS(app)
server = 'LAPTOP-MTEB9CR1\SQLEXPRESS'
database = 'hello'
driver = 'ODBC Driver 17 for SQL Server'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{server}/{database}?driver={driver};Trusted_Connection=yes;'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(db)

@app.route('/insert_data', methods=['POST'])
def create_table():
    try:
        # Connect to the MSSQL database
        
        conn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        user_data = request.get_json()
        # Get the table name, columns, and values from the request
        FirstName = user_data['FirstName']
        LastName = user_data['LastName']
        Gender = user_data['Gender']
        Country = user_data['Country']
        Age = int(user_data['Age'])
        Id = int(user_data['Id'])
        Date = user_data['Date']
        print('Connecting to MSSQL database')
        """table_name = user_data['tableName']
        columns = [f'{column.strip()} VARCHAR(255)' for column in user_data['columns'].split(',')]

        values = [value.strip() for value in user_data['values'].split(',')]

        # Generate the CREATE TABLE query
        create_table_query = f'IF NOT EXISTS (SELECT * FROM sysobjects WHERE name=\'{table_name}\' AND xtype=\'U\') ' \
                             f'CREATE TABLE {table_name} ({", ".join(columns)});'"""
        # Execute the SELECT query
        # Perform data insertion
        insert_query = "INSERT INTO hello.dbo.person (hell, FirstName,LastName,Gender,Country,Age,Date,Id) VALUES ( ?,?,?,?,?,?,?,?)"
        record_to_insert = (55, FirstName,LastName,Gender,Country,Age,Date,Id)
        cursor.execute(insert_query, record_to_insert)

        query = "SELECT * FROM hello.dbo.person"
        cursor.execute(query)
        
        # Retrieve all rows from the result set
        rows = cursor.fetchall()

# Print the retrieved data
        for row in rows:
            print(row)


        """
        # Execute the CREATE TABLE query
        cursor.execute(create_table_query)
        print('table created successfully')
        # Insert the values into the table
        placeholders = ', '.join(['?' for _ in columns])
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders});"
        cursor.execute(insert_query, values)"""

        # Commit the changes
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Table created (if not exist) and values inserted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})
    


if __name__ == '__main__':
    app.run(debug=True)    