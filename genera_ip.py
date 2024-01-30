#!/usr/bin/env python3
import ipaddress
import argparse

def generate_ip_list(start_ip, count):
    start_ip = ipaddress.ip_address(start_ip)
    return [str(start_ip + i) for i in range(count)]

def read_ips_from_file(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

def save_to_file(ip_list, file_name, append=False):
    mode = 'a' if append else 'w'
    with open(file_name, mode) as file:
        for ip in ip_list:
            file.write(ip + '\n')

def main():
    parser = argparse.ArgumentParser(description='Genera un elenco di indirizzi IP.')
    parser.add_argument('-s', '--start_ip', type=str, help='Indirizzo IP iniziale')
    parser.add_argument('-c', '--count', type=int, help='Numero di indirizzi IP da generare')
    parser.add_argument('-o', '--output', type=str, help='Salva l\'elenco in un file')
    parser.add_argument('-a', '--append', action='store_true', help='Appendi all\'elenco esistente invece di sovrascriverlo')
    parser.add_argument('-f', '--file', type=str, help='Leggi gli indirizzi IP da un file')

    args = parser.parse_args()

    # Controllo se sono stati forniti parametri obbligatori
    if not (args.start_ip or args.file) or not args.count:
        parser.print_help()
        return

    if args.file:
        start_ips = read_ips_from_file(args.file)
    else:
        start_ips = [args.start_ip]

    all_generated_ips = []
    for start_ip in start_ips:
        generated_ips = generate_ip_list(start_ip, args.count)
        all_generated_ips.extend(generated_ips)
        if not args.output:
            for ip in generated_ips:
                print(ip)

    if args.output:
        save_to_file(all_generated_ips, args.output, append=args.append)
        action = "aggiunto a" if args.append else "salvato in"
        print(f"L'elenco è stato {action} '{args.output}'")

if __name__ == '__main__':
    main()
