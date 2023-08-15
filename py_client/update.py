import requests

#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/products/5/update/"

data = {
    'title' : "update 4",
    'price' : 40
}

get_response = requests.put(endpoint ,json=data) 

print(get_response.json())
#JavaScrip Object Nototion ~ Python Dict