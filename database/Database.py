import sqlite3

class Database:

    # # properties
    Connection = object()
    Cursor = object()

    # # funcs
    def __init__(self, database_name:str):
        self.Connection = sqlite3.connect(database_name)
        self.Cursor = self.Connection.cursor()

    # send a query to the database
    def Get_Query(self, query:str, auto_commit:bool = True):
        self.Cursor.execute(query)

        if auto_commit : self.Perform_Queries()

    # run the queries that sent before
    def Perform_Queries(self):
        self.Connection.commit()

    # close the connection of db
    def Close_database(self):
        self.Connection.close()
