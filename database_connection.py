import pyodbc
import pandas as pd

def upload_file(file_name):
    data = pd.read_csv(file_name)
    df = pd.DataFrame(data)

    cnxn_str = ("Driver={SQL Server};"
            "Server=ServerName];"
            "Database=General_Sales;"
            "Trusted_Connection=yes;")

    cnxn = pyodbc.connect(cnxn_str)

    cursor = cnxn.cursor()

    cursor.execute('''
    DELETE FROM Sales
    ''')

    for row in df.itertuples():
        cursor.execute('''
            INSERT INTO Sales (OrderId, FirstName, LastName, Date, Product, ProductCount)
            VALUES (?,?,?,?,?,?)
            ''',
            row.OrderId, 
            row.FirstName,
            row.LastName,
            row.Date,
            row.Product,
            row.Count
        )

    cnxn.commit()