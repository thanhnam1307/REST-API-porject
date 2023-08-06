from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django 
    # print(dir(request))
    # request.body 
    print(request.GET)
    print(request.POST)

    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of json data -> Python dict
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
