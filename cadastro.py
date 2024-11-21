import pyodbc
import hashlib

server = 'dbcadastro2024h2.database.windows.net'
database = 'dbcadastro2024h2'
username = 'dbcadastrouser'
password = 'D6hxXlsLVy9sBPxyi'

#
#export AZURE_SQL_CONNECTIONSTRING='Driver={ODBC Driver 18 for SQL Server};Server=tcp:<database-server-name>.database.windows.net,1433;Database=<database-name>;UID=<user-name>;PWD=<user-password>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
#pyodbc.connect(f'DRIVER={driver};SERVER=tcp:{server};PORT=1433;DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30')

# Create the connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Function to register a new user
def register_user(name, email, password):
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Users WHERE Name = ?", (name,))
            if cursor.fetchone()[0] > 0:
                raise Exception("User with this name already exists.")
            cursor.execute("INSERT INTO Users (Name, Email, Password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            print("User registered successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Function to get user input
def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password = hashed_password
    return name, email, password

# Function to retrieve user data by name
def retrieve_user_by_name(name):
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Name, Email, Password FROM Users WHERE Name = ?", (name,))
            row = cursor.fetchone()
            if row:
                print(f"Name: {row[0]}, Email: {row[1]}, Password: {row[2]}")
            else:
                print("User not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
def menu():
    print("1. Register a new user")
    print("2. Retrieve an existing user")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == '1':
            name, email, password = get_user_input()
            register_user(name, email, password)
        elif choice == '2':
            retrieve_name = input("Enter the name of the user to retrieve: ")
            retrieve_user_by_name(retrieve_name)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
