# ShoSubFinder
# Coded By: Abid Ahmad
# Version: 1.0

import argparse
import yaml
from shodan import Shodan
import sys
import os
import time

def load_api_key():
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            return config['shodan_api_key']
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(1)

def combine_results(*args):
    combined = set()
    for result in args:
        combined.update(result)
    return list(combined)

def save_results(filename, results):
    with open(filename, 'w') as f:
        for item in results:
            f.write("%s\n" % item)

def main():
    banner = r"""
   _____ __          _____       __    _______           __         
  / ___// /_  ____ / ___/__  __/ /_  / ____(_)___  ____/ /__  _____
  \__ \/ __ \/ __ \\__ \/ / / / __ \/ /_  / / __ \/ __  / _ \/ ___/
 ___/ / / / / /_/ /__/ / /_/ / /_/ / __/ / / / / / /_/ /  __/ /    
/____/_/ /_/\____/____/\__,_/_.___/_/   /_/_/ /_/\__,_/\___/_/     
                                                        v1.0
              Coded By Abid Ahmad { MrNeutr1n0 }
    """
    warnings = (
        "[WARN] - Use responsibly. Your actions are your own.",
        "[WARN] - The developer disclaims any liability for misuse or damage."
    )

    print(banner)
    for warning in warnings:
        print(warning)

    parser = argparse.ArgumentParser(
        description='      ShoSubFinder - Find Subdomains from Shodan ',
        epilog="EXAMPLES:\n"
               "Use -h or --help for more information.\n"
               "python shosubfinder.py -d example.com -o results.txt\n"
               "python shosubfinder.py -org 'Example Org' -o results.txt\n"
               "python shosubfinder.py -d example.com -asn 'AS1234' -org 'Example Org' -o results.txt",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-d', '--domain', help='Domain/hostname to search.')
    parser.add_argument('-org', '--organization', help='Organization to search (enclose in quotes).')
    parser.add_argument('-asn', '--asn', help='ASN number to search (enclose in quotes).')
    parser.add_argument('-o', '--output', help='Output file name.', required=True)

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        print("\nEXAMPLES:")
        print("python shosubfinder.py -d example.com -o results.txt")
        print("python shosubfinder.py -org 'Example Org' -o results.txt")
        print("python shosubfinder.py -d example.com -asn 'AS1234' -org 'Example Org' -o results.txt")
        sys.exit(1)

    api = Shodan(load_api_key())
    limit = 1000
    counter = 0
    temp_results = []
    start_time = time.time()

    if args.domain:
        domain_query = f'hostname:"{args.domain}" 200'
        for banner in api.search_cursor(domain_query):
            for hostname in banner['hostnames']:
                if args.domain in hostname:
                    temp_results.append(hostname)
            counter += 1
            if counter >= limit:
                break
        domain_results = temp_results.copy()
        temp_results.clear()

    if args.organization:
        org_query = f'org:"{args.organization}" 200'
        for banner in api.search_cursor(org_query):
            for hostname in banner['hostnames']:
                temp_results.append(hostname)
            counter += 1
            if counter >= limit:
                break
        org_results = temp_results.copy()
        temp_results.clear()

    if args.asn:
        asn_query = f'asn:"{args.asn}" 200'
        for banner in api.search_cursor(asn_query):
            for hostname in banner['hostnames']:
                temp_results.append(hostname)
            counter += 1
            if counter >= limit:
                break
        asn_results = temp_results.copy()
        temp_results.clear()

    final_results = combine_results(*(filter(None, [domain_results if args.domain else None, org_results if args.organization else None, asn_results if args.asn else None])))

    save_results(args.output, final_results)

    end_time = time.time()  
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    print(f"[INFO] - Results have been saved to {args.output}")
    print(f"[INFO] - Found {len(final_results)} of subdomains in {minutes} minutes and {seconds} seconds")

if __name__ == "__main__":
    main()
