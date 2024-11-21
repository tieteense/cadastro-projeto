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
def register_user(nome, sobrenome, apelido):
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Users WHERE Nome = ?", (nome,))
            if cursor.fetchone()[0] > 0:
                raise Exception("Usuario já existe com este nome.")
            cursor.execute("INSERT INTO Users (Nome, Sobrenome, Apelido) VALUES (?, ?, ?)", (nome, sobrenome, apelido))
            conn.commit()
            print("Usuario registrado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

# Function to get user input
def get_user_input():
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")
    apelido = input("Digite o seu apelido: ")
    return nome, sobrenome, apelido

# Function to retrieve user data by name
def retrieve_user_by_name(nome,sobrenome):
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Nome, Sobrenome, Apelido FROM Users WHERE Nome = ? AND Sobrenome = ?", (nome,sobrenome))
            row = cursor.fetchone()
            if row:
                print(f"Nome: {row[0]}, Sobrenome: {row[1]}, Apelido: {row[2]}")
            else:
                print("Usuario não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

# Example usage
def menu():
    print("1. Registrar um novo usuário")
    print("2. Consultar um usuário existente")
    print("3. Sair")
    choice = input("Escolha uma opção: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == '1':
            nome, sobrenome, apelido = get_user_input()
            register_user(nome, sobrenome, apelido)
        elif choice == '2':
            retrieve_nome = input("Digite o nome do usuario a ser consultado: ")
            retrieve_sobrenome = input("Digite o sobrenome do usuario a ser consultado: ")
            retrieve_user_by_name(retrieve_nome,retrieve_sobrenome)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
