import requests

api_key = "a364316757273d1c7f7cd59850e8e674"

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#print(weather_data.json())
if weather_data.json()['cod'] == "404":
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f'The weather in {user_input} is {weather}')
    print(f"The temperature is {temp}")
