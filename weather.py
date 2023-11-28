import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # 온도를 섭씨로 받아오기 위해 설정
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    api_key = "5dec5ab39ee52b82243ff8fbf159e2af"
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display_weather(weather_data)