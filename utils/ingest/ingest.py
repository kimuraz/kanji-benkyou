import requests
import json
from time import sleep

ELASTIC = 'http://localhost:9200'
INDEX = 'kanjis'

with open('./data.json') as f:
   data = json.load(f)
   for idx, k in enumerate(data['kanjis']):
       res = requests.post('{}/{}/_doc/'.format(ELASTIC, INDEX), data=json.dumps(data['kanjis'][k], ensure_ascii=False).encode(), headers={'content-type': 'application/json'})
       print('{} CODE: {} ({}/{})'.format(k, res.status_code, idx+1, len((data['kanjis']))))
       if res.status_code != 201:
           print(res.json())
       sleep(0.05)
