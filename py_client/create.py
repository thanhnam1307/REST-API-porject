import requests

#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title" : "this field is done"
}

get_response = requests.post(endpoint ,json=data) 

print(get_response.json())
#JavaScrip Object Nototion ~ Python Dict