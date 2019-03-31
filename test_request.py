import requests
import random
import time
import requests
import json


def randomize():
    bool = random.choice([True, False])
    return bool

while True:
    time.sleep(0.3)    
    bool = randomize()
    for i in range(10):    
        bool = str(bool)   
        payload = {'cam1': bool}          
        r = requests.post('http://192.168.15.23:8080/cam', data=payload)
        print(r.url)
        # print(r.text)
        print(bool)
        time.sleep(0.5)