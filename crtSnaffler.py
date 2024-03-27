#!/usr/bin/env python3
import requests
import argparse

# Colors & Font Options
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RESET = "\033[0m"
BOLD = "\033[1m"


# Ascii banner ... because we all need an ascii banner
def printBanner():

    asciiArt = C_GREEN + """
 ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
||C |||r |||t |||S |||n |||a |||f |||f |||l |||e |||r ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

        """ + C_RESET
    print(asciiArt)

# Prints Banner
printBanner()

parser = argparse.ArgumentParser(description="Retrieve uniqued common names via certificate discovery from crt.sh for a given domain.")
parser.add_argument("-d", "--domain", help="example: crtsnaffler.py -d example.com", required=True)
args = parser.parse_args()

domain_name = args.domain

url = "https://crt.sh/?q=%25.{}&output=json".format(domain_name)
response = requests.get(url)

if not response.content:
    print("No certificates found for {}.".format(domain_name))
    exit()

common_names = set()
for cert in response.json():
    common_name = cert['name_value']
    common_names.add(common_name)

for common_name in common_names:
    print(common_name)

output_file = "common_names_{}.txt".format(domain_name)
with open(output_file, "w") as f:
    for common_name in common_names:
        f.write(common_name + "\n")

print(C_YELLOW + BOLD + "Unique common names saved to:", output_file)
