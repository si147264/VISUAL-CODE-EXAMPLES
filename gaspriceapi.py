import requests

base_url = "http://api.collectapi.com/gasPrice/stateUsaPrice?state=WA"
headers = {
    'content-type': "application/json",
    'authorization': "enter your api_key""
}


response = requests.get(base_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
