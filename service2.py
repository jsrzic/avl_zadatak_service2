import requests
import sys
import os

def main():
    SERVICE1_ALIAS = os.getenv('SERVICE1_ALIAS')
    SERVICE1_PORT = os.getenv('SERVICE1_PORT')
    HASH_FUNCTION = os.getenv('HASH_FUNCTION')
    SERVICE1_URL = f'http://{SERVICE1_ALIAS}:{SERVICE1_PORT}'

    message = requests.get(sys.stdin.readline()).text

    data = [HASH_FUNCTION, message]

    # komentar
    print(requests.post(SERVICE1_URL, data="\n".join(data)).text)

if __name__ == "__main__":
    main()