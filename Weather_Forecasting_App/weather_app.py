import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    print(data)  # Add this line to print the entire API response
    
    if data["cod"] != "404":
        if "main" in data:
            main = data["main"]
            temperature = main["temp"] - 273.15
            weather_desc = data["weather"][0]["description"]
            print(f"Temperature: {temperature:.2f}°C")
            print(f"Weather: {weather_desc}")
        else:
            print("Unexpected response format from the API. Please check the API documentation.")
    else:
        print("City not found. Please check the spelling.")



if __name__ == "__main__":
    api_key = "7833e384b09249b94c0fb90339d7dbcc"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)
