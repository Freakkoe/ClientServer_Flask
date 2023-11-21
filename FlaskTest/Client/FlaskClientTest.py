import requests
url = "http://localhost:5000/Get_data"

param = {"param1": "value1", "param2": "value2"}

response = requests.get(url, params=param)

if response.status_code==200:
    data = response.json()
    print (data) 