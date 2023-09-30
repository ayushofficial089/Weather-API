import requests
import json


API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Failed to retrieve weather data.")
        return None

def get_temperature(data, datetime):
    for entry in data['list']:
        if entry['dt_txt'] == datetime:
            return entry['main']['temp']
    return None

def get_wind_speed(data, datetime):
    for entry in data['list']:
        if entry['dt_txt'] == datetime:
            return entry['wind']['speed']
    return None

def get_pressure(data, datetime):
    for entry in data['list']:
        if entry['dt_txt'] == datetime:
            return entry['main']['pressure']
    return None

def main():
    data = get_weather_data()
    if data is None:
        return

    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(data, datetime)
            if temperature is not None:
                print(f"Temperature at {datetime}: {temperature}°C")
            else:
                print("Data not found for the given date and time.")

        elif option == "2":
            datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(data, datetime)
            if wind_speed is not None:
                print(f"Wind Speed at {datetime}: {wind_speed} m/s")
            else:
                print("Data not found for the given date and time.")

        elif option == "3":
            datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(data, datetime)
            if pressure is not None:
                print(f"Pressure at {datetime}: {pressure} hPa")
            else:
                print("Data not found for the given date and time.")

        elif option == "0":
            break

        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
