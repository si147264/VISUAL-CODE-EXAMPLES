import requests

api_key = "enter you api"
base_url = "https://www.omdbapi.com/"

movie_name = input("Tell me the name of the movie you want to watch: ")


params = {
    "apikey": api_key,
    "s": movie_name  
}

response = requests.get(base_url, params=params)


if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

    
