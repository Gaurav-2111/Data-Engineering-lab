import requests
response = requests.get(base_url,headers=headers)
print(response.status_code)
data = response.json()
print(type(data))
print(data.keys())
