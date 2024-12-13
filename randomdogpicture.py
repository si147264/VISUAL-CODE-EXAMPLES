import requests

base_url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(base_url)


if response.status_code == 200:
    data = response.json()  
  
    print(f"Random Dog Image URL: {data['message']}")
  
else:
    print(f"Error: {response.status_code}")
