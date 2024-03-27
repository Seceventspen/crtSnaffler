# crtSnaffler

## Overview
Welcome to crtSnaffler! This tool is designed to help you retrieve and analyze SSL/TLS certificate information associated with a specific domain. Whether you're a cybersecurity enthusiast, a web administrator, or simply curious about the security of a website, crtSnaffler provides a convenient way to explore the certificates used by a domain.

## How it Works
crtSnaffler is a Python script that leverages the crt.sh database, a well-known resource for certificate transparency logs. By querying crt.sh with a given domain, crtSnaffler collects and organizes certificate information related to that domain. It then extracts the common names (domain names) from these certificates and presents them in a readable format.

### Key Functions

**printBanner()**
This function prints an ASCII art banner to add a touch of flair to the tool. While not crucial to the functionality, it certainly adds some visual appeal!

**Parsing Command-Line Arguments**
crtSnaffler utilizes the argparse library to parse command-line arguments. Specifically, it expects a single argument `-d` or `--domain`, which should be followed by the domain name you want to investigate. This allows for easy customization and usage from the command line.

**Fetching and Processing Certificate Information**
The core functionality of crtSnaffler involves fetching certificate information from `crt.sh` and processing it. After constructing the appropriate URL based on the provided domain, the script sends an HTTP GET request to crt.sh. Upon receiving the response, it parses the JSON data and extracts the common names (domain names) from the certificates.

**Writing Common Names to a File**
To ensure easy access and reference to the extracted domain names, crtSnaffler writes them to a text file named `common_names_{domain}.txt`. This file serves as a record of the unique domain names associated with the queried domain.

## Expected Outcome
Upon running crtSnaffler with the desired domain name provided as a command-line argument, you can expect the following outcomes:

A list of unique domain names associated with the queried domain will be displayed in the console.
The same list of unique domain names will be saved to a text file `(common_names_{domain}.txt)` in the current directory.
A message indicating the path to the output file will be printed in the console for easy reference.

## Conclusion
crtSnaffler offers a straightforward yet powerful solution for exploring SSL/TLS certificate information associated with a domain. Whether you're conducting security assessments, investigating certificate configurations, or simply satisfying your curiosity, crtSnaffler is a handy tool to have in your arsenal. So go ahead, give it a try, and uncover the secrets hidden within SSL/TLS certificates!
