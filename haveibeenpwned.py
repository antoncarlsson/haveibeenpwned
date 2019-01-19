#!/usr/bin/env python3
from hashlib import sha1
from getpass import getpass
import requests
import sys

def main():
    password = getpass()
    sha1_hash = sha1(password.encode('utf-8')).hexdigest().upper()
    sha1_hash_prefix = sha1_hash[0:5]
    url = 'https://api.pwnedpasswords.com/range/' + sha1_hash_prefix

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(error)
        sys.exit(1)

    count = 0
    for line in response.text.split('\r\n'):
        if sha1_hash == sha1_hash_prefix + line.split(':')[0]:
            count = line.split(':')[1]
            break
    print('You have been pwned', count, 'times.')


if __name__ == '__main__':
    main()
