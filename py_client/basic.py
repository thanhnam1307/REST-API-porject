import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://www.facebook.com/"

get_response = requests.get(endpoint) #Http request
print(get_response.text)#print raw text response 
