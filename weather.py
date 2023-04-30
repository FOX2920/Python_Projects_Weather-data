import requests


class Location:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS locations (
              id INT AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(255),
              country VARCHAR(255),
              longitude FLOAT,
              latitude FLOAT
            )
        '''
        self.db_connection.connect()
        self.db_connection.insert_data(query, None)
        self.db_connection.close()

    def insert_data(self, data):
        query = '''
            INSERT INTO locations (name, country, longitude, latitude)
            VALUES (%s, %s, %s, %s)
        '''
        self.db_connection.connect()
        self.db_connection.insert_data(query, data)
        self.db_connection.close()

    def get_location_id(self, name):
        query = "SELECT id FROM locations WHERE name=%s"
        self.db_connection.connect()
        cursor = self.db_connection.connection.cursor()
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        cursor.close()
        self.db_connection.close()

        if result:
            return result[0]
        else:
            return None


class Weather:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS weather (
              id INT AUTO_INCREMENT PRIMARY KEY,
              location_id INT,
              location_name VARCHAR(255),
              temperature FLOAT,
              humidity FLOAT,
              pressure FLOAT,
              weather_type ENUM('clear', 'clouds', 'rain', 'drizzle', 'thunderstorm', 'snow', 'mist', 'smoke', 'haze', 'dust', 'fog', 'sand', 'ash', 'squall', 'tornado') NOT NULL,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              FOREIGN KEY (location_id) REFERENCES locations(id)
            )
        '''
        self.db_connection.connect()
        self.db_connection.insert_data(query, None)
        self.db_connection.close()

    def insert_data(self, location_name, data):
        query = '''
            INSERT INTO weather (location_id, location_name, temperature, humidity, pressure, weather_type)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        self.db_connection.connect()
        self.db_connection.insert_data(query, (data[0], location_name, data[1], data[2], data[3], data[4]))
        self.db_connection.close()
