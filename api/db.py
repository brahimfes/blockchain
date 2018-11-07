import mysql.connector
import json


class MysqlDatabase:
    __user = None
    __password = None
    __host = None
    __database = None
    __connection = None
    __session = None

    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def open(self):
        connection = mysql.connector.connect(
            user=self.__user, password=self.__password, host=self.__host, database=self.__database)
        self.__connection = connection
        self.__session = connection.cursor()

    def close(self):
        self.__session.close()
        self.__connection.close()

    def execute(self, query):
        self.open()
        self.__session.execute(query)
        row_headers = [x[0] for x in self.__session.description]
        result = self.__session.fetchall()
        json_data = []
        for resultItem in result:
            json_data.append(dict(zip(row_headers, resultItem)))
        self.close()
        return json.dumps(json_data)

    def insert(self, query):
        self.open()
        self.__session.execute(query)
        rowid = self.__session.lastrowid
        self.__connection.commit()
        self.close()
        return rowid
