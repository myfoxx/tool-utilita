import hashlib
import requests
import sys
import argparse

# Put here your API KEY
API_KEY = 'YOUR_HIBP_API_KEY'

def hash_password(password):
    sha1hash = hashlib.sha1(password.encode()).hexdigest().upper()
    return sha1hash

def check_pwned(password):
    sha1password = hash_password(password)
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = requests.get('https://api.pwnedpasswords.com/range/' + first5_char, headers={'hibp-api-key': API_KEY})
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}")
    
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return True, count
    
    return False, 0

def process_passwords(passwords):
    pwned_passwords = []
    for password in passwords:
        is_pwned, count = check_pwned(password)
        if is_pwned:
            pwned_passwords.append((password, count))

    return pwned_passwords

def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_to_file(output_file, pwned_passwords):
    with open(output_file, 'w') as file:
        for password, count in pwned_passwords:
            file.write(f"Password: {password} has been breached {count} time's .\n")

def main():
    parser = argparse.ArgumentParser(description="Check if passwords have been pwned. Script by Myfox")
    parser.add_argument('-p', '--password', help="Check a single password")
    parser.add_argument('-f', '--file', help="File path containing a list of passwords")
    parser.add_argument('-o', '--output', help="Output file to write pwned passwords")

    args = parser.parse_args()

    if not args.password and not args.file:
        parser.print_help()
        sys.exit()

    passwords = [args.password] if args.password else read_passwords_from_file(args.file)

    pwned_passwords = process_passwords(passwords)

    if args.output:
        write_to_file(args.output, pwned_passwords)
    else:
        for password, count in pwned_passwords:
            print(f"Password: {password} has been breached {count} time's.")

    if not pwned_passwords:
        print("No password in the list has been compromised.")

if __name__ == "__main__":
    main()
