from flask import Flask, request, jsonify
import pandas as pd
import pyodbc
from flask_cors import CORS
from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app,)
# Replace with your SQL Server connection details
server = 'LAPTOP-MTEB9CR1\SQLEXPRESS'
database = 'hello'
driver = '{ODBC Driver 17 for SQL Server}'

    

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file'] 
    df = pd.read_excel(file, engine='openpyxl') # Get the uploaded file
    print(df)
    
    if file:
        
        # Establish the connection using Windows authentication
        conn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        count = 1
        for index, row in df.iterrows():
            # Replace 'Column1' with the actual column name in your Excel file
            FirstName = row['FirstName']
            LastName = row['LastName']
            Gender = row['Gender']
            Country = row['Country']
            Age = int(row['Age'])
            Date = str(row['Date'])
            Id = int(row['Id'])
              # Replace 'Column2' with the actual column name in your Excel file

            # ... Add more values as needed
            
            record_to_insert = (count, FirstName,LastName,Gender,Country,Age,Date,Id)

            query = "INSERT INTO hello.dbo.person (hell, FirstName,LastName,Gender,Country,Age,Date,Id) VALUES ( ?,?,?,?,?,?,?,?)"  # Replace 'your_table_name' and 'column1', 'column2' with the actual table and column names
            cursor.execute(query,record_to_insert) 
            count + 1

        """# Get the column names and data types from the Excel file
        column_names = df.columns.tolist()
        
        # Create table if it doesn't exist
        create_table_query = f"IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[YourTableName]') AND type in (N'U')) "
        create_table_query += f"BEGIN CREATE TABLE YourTableName ("

        for column_name in column_names:
            data_type = df[column_name].dtype
            if data_type == 'int64':
                create_table_query += f'{column_name} INT, '
            elif data_type == 'float64':
                create_table_query += f'{column_name} FLOAT, '
            else:
                create_table_query += f'{column_name} NVARCHAR(255), '

        create_table_query = create_table_query.rstrip(', ')
        create_table_query += ') END'

        # Execute the query
        cursor.execute(create_table_query)


        # Insert data into SQL Server table
        for index, row in df.iterrows():
            insert_query = f"INSERT INTO YourTableName ({', '.join(column_names)}) VALUES ({', '.join(['?'] * len(column_names))})"
            cursor.execute(insert_query, *row)"""
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'File uploaded successfully.'})
    else:
        return jsonify({'error': 'No file uploaded.'}), 400
    

@app.route('/insert_data', methods=['POST'])
def create_table():
    try:
        # Connect to the MSSQL database
        conn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        # Get the table name, columns, and values from the request
        table_name = request.json['tableName']
        columns = [f'{column.strip()} VARCHAR(255)' for column in request.json['columns'].split(',')]

        values = [value.strip() for value in request.json['values'].split(',')]

        # Generate the CREATE TABLE query
        create_table_query = f'IF NOT EXISTS (SELECT * FROM sysobjects WHERE name=\'{table_name}\' AND xtype=\'U\') ' \
                             f'CREATE TABLE {table_name} ({", ".join(columns)});'

        # Execute the CREATE TABLE query
        cursor.execute(create_table_query)
        print('table created successfully')
        # Insert the values into the table
        placeholders = ', '.join(['?' for _ in columns])
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders});"
        cursor.execute(insert_query, values)

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
    