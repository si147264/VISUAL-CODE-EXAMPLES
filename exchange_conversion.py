import requests
api_key= "4rgCNqZClGoGyIQIx00qRu:0kEueqq722pKVLLK6dsOx2"
base_url="https://api.collectapi.com/economy/exchange"

base_currency=input("enter your currency unit which you want to exchange").upper()
target_currency=input("enter your target currency which you want to exchange").upper()

headers={"Authorization":f"apikey {api_key}",
         "Content-Type":"application/json"}

params={"base":base_currency,
        "to":target_currency}



response = requests.get(base_url, headers=headers, params=params)



if response.status_code==200:
    print("request is successful")
    data=response.json()
    rate=data["conversion_rates"].get("target_currency")
    print(data)
    if rate:
        print(f"{base_currency} is converted into  {target_currency} at the rate of {rate:.2f}" )
    else:
        print(f"Conversion rate for {base_currency}to {target_currency} is not available")
else:
    print("Api request failed")