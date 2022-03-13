import requests

def get_data(url):
    r = requests.get(url)
    return r.content