import requests

#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"


get_response = requests.get(endpoint ,params={"product_id":123}) #Http request
#print(get_response.text)#print raw text response 
#print(get_response.status_code)
#HTTP Request ->HTML
#REST API HTTP Request ->JSON
print(get_response.json())
#JavaScrip Object Nototion ~ Python Dict