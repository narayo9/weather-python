import requests

API_KEY = '96ec1c513612947553e8887d7c173e8c'  # OpenWeatherMap의 API 키를 여기에 입력하세요
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_seoul_weather():
    city_name = "Seoul"
    complete_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
    response = requests.get(complete_url)

    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]

        temperature = main_data["temp"] - 273.15  # Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]

        print(f"{city_name:-^30}")
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Atmospheric Pressure: {pressure} hPa")


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(city_name):
    complete_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
    response = requests.get(complete_url)

    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]

        temperature = main_data["temp"] - 273.15  # Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]

        print(f"{city_name:-^30}")
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Atmospheric Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description}")
        print("-----------------------------")

    else:
        print("City not found!")


if __name__ == "__main__":
    # 서울을 보여줘야 함
    city_name = "Seoul"
    get_weather(city_name)
