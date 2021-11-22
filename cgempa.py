#!/usr/bin/env python3
import itertools
import threading
import time
import sys
import requests
import json
import os

os.system('clear')

a = ("""
   ___
  / __\__ _  ___ _ __ ___  _ __   __ _
 / /  / _` |/ _ \ '_ ` _ \| '_ \ / _` |
/ /__| (_| |  __/ | | | | | |_) | (_| |
\____/\__, |\___|_| |_| |_| .__/ \__,_|
      |___/               |_|

------Cek Informasi Gempa Terbaru------

Twitter : alfin_kresna
IG      : alfin.kresna_
""")
print(a)

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rMemuat Data ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

time.sleep(3)
done = True
print()
print()
response = requests.get("https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json")
json_response = response.json()
pretty_response = json.dumps(json_response, indent=4)
pretty_response = json.dumps(response.json(), indent=4)
print(pretty_response)
print()
