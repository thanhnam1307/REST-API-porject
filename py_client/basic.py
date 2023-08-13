import requests

#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"


get_response = requests.get(endpoint ,json={'product_id':123}) 


print(get_response.json())
#JavaScrip Object Nototion ~ Python Dict