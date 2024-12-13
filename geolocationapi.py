import requests

base_url="https://api.iplocation.net/"
params= {"ip":"enter your IP Adress"}

response=requests.get(base_url,params=params)

if response.status_code==200:
    data=response.json()
    print(data)
    print(f" IP:{data['ip']}")
    print(f"IP no:{data['ip_number']}")
    print(f"counrty:{data['country_name']}")
    print(f"response_message:{data.get('response_message','not_available')}")
else:
    print(f"error:{response.status_code}")
    