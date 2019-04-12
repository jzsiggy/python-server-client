import requests
import random
import time
import requests
import json
import sys


def randomize():
    bool = random.choice([True, False])
    return bool

while True:
    # time.sleep(0.1)    
    bool = randomize()
    for i in range(10):    
        bool = str(bool)   
        try:    
            payload = {'cam0': bool}          
            r = requests.post('http://127.0.0.1:8080/cam', data=payload)
        except:
            sys.exit(1)

        print(r.url)
        # print(r.text)
        print(bool)
        time.sleep(0.5)