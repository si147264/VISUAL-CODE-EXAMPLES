import requests
base_url="https://www.omdbapi.com/?i=tt3896198&apikey=4cde8281"
response=requests.get(base_url)
if response.status_code==200:
    data=response.json()
    print(data)
    print("Film_name:",data["Title"])
    print("Year:",data["Year"])
    print("score rated:",data["Rated"])
    print("Film genre:",data["Genre"])

else:
    print("Invalid API")
