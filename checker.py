import warnings
import requests
import hashlib
import getpass
import sys

def request_pwn_API(query):
    url = f'https://api.pwnedpasswords.com/range/{query}'
    
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError('An error occurred while requesting API.')

    return response

def get_password_hash(password):
    password_utf8 = password.encode('utf-8')
    sha1_hash = hashlib.sha1(password_utf8)
    hash_digest = sha1_hash.hexdigest().upper()
    return hash_digest

def get_hash_pwned_times(test_hash_suffix, pwned_hashes):
    for line in pwned_hashes:
        pwned_hash_suffix, pwned_times = line.split(':')
        if pwned_hash_suffix == test_hash_suffix:
            return pwned_times
    return 0

def get_password_pwned_times(password_str):
    password_hash = get_password_hash(password_str)
    hash_first5chars = password_hash[:5]
    hash_suffix = password_hash[5:]

    pwned_response_text = request_pwn_API(hash_first5chars).text
    pwned_times = get_hash_pwned_times(
        hash_suffix,
        pwned_response_text.splitlines()
    )

    return pwned_times

def main():
    while True:
        with warnings.catch_warnings():
            warnings.filterwarnings('error', category=getpass.GetPassWarning)
            try:
                password_str = getpass.getpass()
            except getpass.GetPassWarning as w:
                print(
                    'Cannot securely obtain password from the terminal. '
                    'Aborting.'
                )
                return
            except KeyboardInterrupt:
                print('Exiting the program.')
                return

        pwned_times = get_password_pwned_times(password_str)
        if pwned_times:
            print(f'Password found {pwned_times} times in the database.')
        else:
            print('Password was not found in the database.')

if __name__ == '__main__':
    main()
