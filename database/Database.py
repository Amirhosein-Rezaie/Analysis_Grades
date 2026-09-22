import sqlite3

class Database:

    # # properties
    __Connection = object()
    __Cursor = object()

    # # funcs
    def __init__(self, database_name:str):
        self.__Connection = sqlite3.connect(database_name)
        self.__Cursor = self.__Connection.cursor()

    # send a query to the database
    def Get_Query(self, query:str, auto_commit:bool = True):
        self.__Cursor.execute(query)

        if auto_commit : self.Perform_Queries()

    # run the queries that sent before
    def Perform_Queries(self):
        self.__Connection.commit()

    # close the __Connection of db
    def Close_database(self):
        self.__Connection.close()
