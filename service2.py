import requests
import sys
import os

SERVICE1_URL = os.getenv('SERVICE1_URL')
HASH_FUNCTION = os.getenv('HASH_FUNCTION')

message = requests.get(sys.stdin.readline()).text

data = [HASH_FUNCTION, message]

print(requests.post(SERVICE1_URL, data="\n".join(data)).text)