import requests
book=input("which book do you want to read ?").upper()
base_url=f"https://www.googleapis.com/books/v1/volumes?q={book}"
response=requests.get(base_url)

if response.status_code==200:
    data=response.json()
    print(data)

else:
 print(f"Error: response.status_code = {response.status_code}")