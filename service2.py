import requests
import sys
import json

def main():
    with open(sys.argv[1], 'r') as config_file:
        config = json.load(config_file)

    SERVICE1_ALIAS = config['SERVICE1_ALIAS']
    SERVICE1_PORT = config['SERVICE1_PORT']
    HASH_FUNCTION = config['HASH_FUNCTION']
    SERVICE1_URL = f'http://{SERVICE1_ALIAS}:{SERVICE1_PORT}'

    message = requests.get(sys.stdin.readline()).text

    data = [HASH_FUNCTION, message]

    print(requests.post(SERVICE1_URL, data="\n".join(data)).text)

if __name__ == "__main__":
    main()