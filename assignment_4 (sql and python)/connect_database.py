import os
import mysql.connector
from mysql.connector import Error


class ConnectDatabase:

    def __init__(self, database):
        self.host = os.environ.get('host', 'localhost')
        self.database = database
        self.user = os.environ.get('db_user')
        self.password = os.environ.get('db_password')
        self.db = None
        self.create_connection()

    def create_connection(self):
        try:
            self.db = mysql.connector.connect(host=self.host,
                                              user=self.user,
                                              password=self.password,
                                              database=self.database)
        except Error as e:
            print(f"Error in connecting to database. Error ms: {e}")

    def get_db(self):
        return self.db
