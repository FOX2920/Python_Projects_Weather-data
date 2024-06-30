# Weather Data Collection & MySQL API Integration

This is a Python application that fetches weather data for a random city using the OpenWeatherMap API and stores the data into a MySQL database.

## Requirements

Before running the application, make sure you have installed:

- Python 3.x
- MySQL Database

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/FOX2920/Python_Projects_Weather-data-test-.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Python_Projects_Weather-data-test-
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:
- Create a new database named `weather`.
- Open the `main.py` file and update the database connection information with your MySQL login details:
    ```python
    db = DatabaseConnection(
        host="your_host",
        username="your_username",
        password="your_password",
        database="weather"
    )
    ```

5. Set up the OpenWeatherMap API key:
- Open the `main.py` file and replace `YOUR_API_KEY` with your actual OpenWeatherMap API key.

## Usage

To run the application, execute the following command:
    ```bash
    python main.py
    ```

The application will perform the following steps:

1. Connect to the MySQL database and create the necessary tables if they do not exist.
2. Fetch a random country and its capital city from the `countriesnow.space` API.
3. Retrieve the weather data for the random city from the OpenWeatherMap API.
4. Insert the location and weather data into the respective tables in the MySQL database.
5. Output a message indicating whether the weather data was successfully inserted into the database.

## Project Structure

- `connection.py`: Contains the `DatabaseConnection` class to manage MySQL database connections.
- `weather.py`: Contains the `Location` and `Weather` classes to create and interact with the corresponding database tables.
- `main.py`: The main script that controls the process of fetching and storing weather data.
- `requirements.txt`: Lists the Python packages required for the project.
