
import requests


base_url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin", 
    "vs_currencies": "usd"  
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
 
    data = response.json()
    print(data)
    if data["bitcoin"]["usd"]>300000:
     data["bitcoin"]["usd"]=300000

else:
 print(f"Error: response.status_code = {response.status_code}")