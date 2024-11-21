import pyodbc

# Define the connection parameters
server = 'dbcadastro2024h2.database.windows.net'
database = 'dbcadastro2024h2'
username = 'dbcadastrouser'
password = 'D6hxXlsLVy9sBPxyi'

# Create the connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Test the connection
try:
    with pyodbc.connect(connection_string) as conn:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")