import json
import urllib.request

def get_payload():
    urllib.request.urlopen('http://127.0.0.1:13333/name/add?add=Jackie')
    response = urllib.request.urlopen('http://127.0.0.1:13333/names')
    payload = json.loads(response.read().decode('utf8'))
    assert payload == "{name : ['Jackie']}"
    print(payload)
    urllib.request.urlopen('http://127.0.0.1:13333/name/remove?remove=Jackie')
    assert payload == "{name : []}"

if __name__ == '__main__':
    get_payload()
