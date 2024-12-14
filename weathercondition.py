import requests
my_api_key="enter your api key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name=input("choose a city")
response=requests.get(base_url,params={
    "q":city_name,
    "appid":my_api_key,
    "units":"metric",
    "lang":"en"
})


if response.status_code==200:
    data=response.json()
   
    city=data["name"]
    temperature=data["main"]["temp"]
    description=data["weather"][0]["description"]
    humidity=data["main"]["humidity"]
    wind_speed=data["wind"]["speed"]
    print(f"name:{"city"}")
    print(f"temperature:{temperature}")
    print(f"description:{description}")
    print(f"wind_speed:{wind_speed}")
else:
    print("there is error")
    print(f"error code:{response.status_code}")

