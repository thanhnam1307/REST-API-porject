import requests

#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/products/1233/"


get_response = requests.get(endpoint) 

print(get_response.json())
#JavaScrip Object Nototion ~ Python Dict