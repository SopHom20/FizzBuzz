import requests
from datetime import datetime
import hashlib

character = input("Enter a Marvel character")
ts = datetime.timestamp(datetime.now())
private_key = 'dd9f636bb9927e657228de86f6fc0047cac8dae3'
public_key = '1c3a6525dc80c14c7fadb474d1bd11c5'
hashkey = hashlib.md5()
hashkey.update(f'{ts}{private_key}{public_key}'.encode())
hashed = hashkey.hexdigest()

parameters = {'apikey': public_key, 'ts': ts, 'hash': hashed, 'name': character}
request = (requests.get('https://gateway.marvel.com/v1/public/characters?', params=parameters)).json()


if request['data']['count'] > 0:
    print("Name: " + request['data']['results'][0]['name'])
    description = request['data']['results'][0]['description']
    if len(description) > 0:
        print("Description: " + request['data']['results'][0]['description'])
    else:
        print("No description provided")
else:
    print("No marvel character was found that matches your input")