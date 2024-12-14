import requests

capital=input("which capital would you like information about?")
base_url= f"https://restcountries.com/v3.1/capital/{capital}"

response=requests.get(base_url)
if response.status_code==200:
    data=response.json()
    print(f"Country Name: {data[0]['name']['common']}")
    print(f"Population: {data[0]['population']}")
else:
    print(f"error:{response.status_code}")
