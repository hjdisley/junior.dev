import requests

def get_data(url):
    '''
    Takes a URL and makes a request to the url using custom headers
    input:
        url (str): URL of a webpage you want to make a request
    output:
        r.content (str): Returns the content of the request in bytes
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://google.com',
        'DNT': '1'
    }
    r = requests.get(url, headers=headers)
    return r.content