import requests

product_id = input("What is product id you want to use?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not is a lavid')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"                
    get_response = requests.delete(endpoint)

    print(get_response.status_code,get_response.status_code==204)
#JavaScrip Object Nototion ~ Python Dict