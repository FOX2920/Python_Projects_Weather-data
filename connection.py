import mysql.connector


class DatabaseConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )

    def close(self):
        if self.connection:
            self.connection.close()

    def insert_data(self, query, data):
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        self.connection.commit()
        cursor.close()
