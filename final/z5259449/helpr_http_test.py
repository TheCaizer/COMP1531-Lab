'''
HTTP tests for the helpr application
'''

import config
import urllib.request
import json
import requests

# Do NOT change this URL! If you need to change the port number, change the
# value in config.py
BASE_URL=f"http://127.0.0.1:{config.PORT}"

def test_queue():
    '''test the queue returns the an empty list at the start'''
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert payload == []
def test_make_request():
    '''test make request woeks and sends into queue'''
    payload = requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234567',
        'description': 'Help me code',
    })
    assert payload.json() == {}
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'waiting'}]
def test_end():
    '''test that end works and clears the queue'''
    requests.delete(f"{BASE_URL}/end")
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == []
def test_remaining():
    '''test remaining and adding mutiple make_request'''
    requests.delete(f"{BASE_URL}/end")
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234567',
        'description': 'Help me code',
    })
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234568',
        'description': 'Final too hard',
    })
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234569',
        'description': 'Final too long',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'waiting'},
                     {'zid': 'z1234568', 'description': 'Final too hard', 'status': 'waiting'},
                     {'zid': 'z1234569', 'description': 'Final too long', 'status': 'waiting'}]
    queryString = urllib.parse.urlencode({
        'zid' : 'z1234569',
    })
    payload = json.load(urllib.request.urlopen(f"{BASE_URL}/remaining?{queryString}"))
    assert payload == {'remaining': 2}
def test_help():
    '''test help'''
    requests.delete(f"{BASE_URL}/end")
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234567',
        'description': 'Help me code',
    })
    requests.post(f"{BASE_URL}/help",json={
        'zid': 'z1234567',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'receiving'}]
def test_resolve():
    '''test resovle'''
    requests.delete(f"{BASE_URL}/end")
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234567',
        'description': 'Help me code',
    })
    requests.post(f"{BASE_URL}/help",json={
        'zid': 'z1234567',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'receiving'}]
    requests.delete(f"{BASE_URL}/resolve", json={
        'zid': 'z1234567',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == []
def test_cancel():
    '''test cancel'''
    requests.delete(f"{BASE_URL}/end")
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234567',
        'description': 'Help me code',
    })
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234568',
        'description': 'Final too long',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'waiting'},
                     {'zid': 'z1234568', 'description': 'Final too long', 'status': 'waiting'}]
    requests.delete(f"{BASE_URL}/cancel", json={
        'zid': 'z1234568',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'waiting'}]
def test_revert():
    '''test revert'''
    requests.delete(f"{BASE_URL}/end")
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234567',
        'description': 'Help me code',
    })
    requests.post(f"{BASE_URL}/make_request", json={
        'zid': 'z1234568',
        'description': 'Final too hard',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'waiting'},
                     {'zid': 'z1234568', 'description': 'Final too hard', 'status': 'waiting'}]
    requests.post(f"{BASE_URL}/help",json={
        'zid': 'z1234568',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'waiting'},
                     {'zid': 'z1234568', 'description': 'Final too hard', 'status': 'receiving'}]
    requests.post(f"{BASE_URL}/revert", json={
        'zid': 'z1234568',
    })
    queue =  json.load(urllib.request.urlopen(f"{BASE_URL}/queue"))
    assert queue == [{'zid': 'z1234567', 'description': 'Help me code', 'status': 'waiting'},
                     {'zid': 'z1234568', 'description': 'Final too hard', 'status': 'waiting'}]