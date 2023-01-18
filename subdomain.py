#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('subdomain.py'))
print('Hello Welcome subdomain Scanner Ali Baykara')
import argparse
import requests
from bs4 import BeautifulSoup

def check_subdomains(domain, output_file):
    subdomains = []
    print("[+] Start scanning")
    try:
        req = requests.get("http://"+domain)
        if req.status_code == 200:
            subdomains.append("http://"+domain)
            print("    [+] Subdomain: ", "http://"+domain)
            soup = BeautifulSoup(req.content, "html.parser")
            for link in soup.find_all("a"):
                link = link.get("href")
                if link.startswith("http"):
                    if domain in link:
                        subdomains.append(link)
                        print("    [+] Subdomain: ", link)
    except:
        pass
    try:
        req = requests.get("https://"+domain)
        if req.status_code == 200:
            subdomains.append("https://"+domain)
            print("    [+] Subdomain: ", "https://"+domain)
            soup = BeautifulSoup(req.content, "html.parser")
            for link in soup.find_all("a"):
                link = link.get("href")
                if link.startswith("https"):
                    if domain in link:
                        subdomains.append(link)
                        print("    [+] Subdomain: ", link)
    except:
        pass
    with open(output_file, 'w') as f:
        for subdomain in subdomains:
            f.write("%s\n" % subdomain)
    print("[+] Discovered subdomains are saved in "+output_file)
    print("[+] Scanning completed")
    return subdomains

parser = argparse.ArgumentParser(description='Subdomain Scanner')
parser.add_argument('-d', '--domain', dest='domain', help='Target Domain')
parser.add_argument('-o', '--output', dest='output', help='Output File')
args = parser.parse_args()

if args.domain:
    if args.output:
        check_subdomains(args.domain, args.output)
    else:
        print("[-] Please provide an output file name.")
else:
    print("[-] Please provide a target domain.")

