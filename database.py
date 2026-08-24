# pyodbc connects Python to databases.
import pyodbc


class Database:

    def __init__(self):
        # Connection details for the local SQL Server database.
        self.connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=.\\SQLEXPRESS;"
            "DATABASE=StudentManagement;"
            "Trusted_Connection=yes;"
        )

    def connect(self):
        # Open and return a database connection.
        return pyodbc.connect(self.connection_string)