import requests

url = "https://ado-officialshop-friedpotato.com/products/Ado26Ao_004V"

r = requests.get(url)

print(r.status_code)

print("SOLD OUT" in r.text)
