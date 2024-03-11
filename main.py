import requests
import random
from connection import DatabaseConnection
from weather import Location, Weather

def get_random_country_and_capital():
    # Send an HTTP request to the API
    response = requests.get('https://countriesnow.space/api/v0.1/countries/capital')

    # Get the list of countries from the response
    countries = response.json()['data']

    # Get a random country and its corresponding capital
    country = random.choice(countries)
    name = country['name']
    capital = country['capital']

    # Return the result as a list of country and capital
    return name, capital

# Set up the database connection
db = DatabaseConnection(
    host=" database.cvjkjhwj5dws.ap-southeast-1.rds.amazonaws.com",
    username="admin",
    password="tranthanhson",
    database="weather"
)
api_key = "YOUR_API_KEY"

# Create the locations and weather tables if they don't exist
location = Location(db)
location.create_table()

weather = Weather(db)
weather.create_table()

# Get a random country and capital
country, city = get_random_country_and_capital()

# Get the weather data for the random city from the OpenWeatherMap API
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extract the relevant weather data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather_type = data["weather"][0]["main"]

    # Insert the weather data into the database
    location.insert_data((city, country, data["coord"]["lon"], data["coord"]["lat"]))
    weather.insert_data(city, (location.get_location_id(city), temperature, humidity, pressure, weather_type))

    print(f"Weather data for {city}, {country} inserted into the database.")
else:
    print("Failed to retrieve weather data from the OpenWeatherMap API.")
