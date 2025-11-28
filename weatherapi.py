import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
city= input("Enter a valid city to get its weather data: ")

weather_api= os.getenv("Weather_api_key")

url=f"http://api.weatherapi.com/v1/current.json?key={weather_api}&q={city}"
url2=f"http://api.weatherapi.com/v1/forecast.json?key={weather_api}&q={city}&days=7"

response= requests.get(url)
response2= requests.get(url2)


weather_data=response.json()
forecast_data=response2.json()


print(f"weather of {weather_data['location']['name']}:")
print(f"temperature: {weather_data['current']['temp_c']} degree celsius")
print(f"the climate is {weather_data['current']['condition']['text']} today")
print("-"*50)

print(f"weather forecast of {weather_data['location']['name']} for the next 7 days:")

forecasts= forecast_data['forecast']['forecastday']

for forecast in forecasts[1:]:
    print(forecast['date'])
    print(f"average temp:{forecast['day']['avgtemp_c']}")
    print(f"the weather will be {forecast['day']['condition']['text']}")
    print(f"sunrise time: {forecast['astro']['sunrise']}")
    print(f"sunset time: {forecast['astro']['sunset']}")
    print("-"*50)










