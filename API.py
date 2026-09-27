
import requests


latitude = float(input("Enter latitude (e.g. 9.56 for Hargeisa): "))
longitude = float(input("Enter longitude (e.g. 44.07 for Hargeisa): "))


url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    "&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
)


response = requests.get(url)


if response.status_code == 200:
    print("Request successful!\n")

   
    data = response.json()

   
    current = data["current"]
    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]
    humidity = current["relative_humidity_2m"]


    print(f"Temperature: {temperature}°C")
    print(f"Wind speed: {wind_speed} km/h")
    print(f"Humidity: {humidity}%")

else:
    
    print(f"Request failed! Status code: {response.status_code}")
    print(response.text)