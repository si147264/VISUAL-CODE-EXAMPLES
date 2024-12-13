import requests
base_url="https://v2.jokeapi.dev/joke/Programming"
response=requests.get(base_url)

if response.status_code==200:
    data=response.json()
    print(f"joke:{data['joke']}")