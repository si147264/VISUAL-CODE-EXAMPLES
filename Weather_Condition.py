import requests
my_api_key="d51825349a41852e754c1a793c223aa1"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name=input("choose a city")
response=requests.get(base_url,params={
    "q":city_name,
    "appid":my_api_key,
    "units":"metric",
    "lang":"en"
})
# These parameter shows information ve its kind sent by Api
# Bu parametreler, API'ye gönderilen bilgileri ve ne tür bir yanıt almak istediğimizi belirtir.

if response.status_code==200:
    data=response.json()
    #Bu metod, Response nesnesinden gelen JSON verisini otomatik olarak bir Python veri yapısına (genellikle bir dict - sözlük) dönüştürür.
    #Böylece, JSON verisini Python ile daha kolay işleyebilirsiniz.
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

