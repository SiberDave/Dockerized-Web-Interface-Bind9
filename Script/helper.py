#! /bin/python3

import requests
import re

# Get the hosts file from network and parse it to csv
def parse_hosts_file(url):
    domains = []
    current_section = None

    response = requests.get(url)
    response.raise_for_status()

    lines = response.text.split('\n')

    for line in lines:
        section_match = re.match(r'^#<(\w.+)>$',line)
        section_end_match = re.match(r'#</(\w.+)>$',line)
        if section_match:
            current_section = section_match.group(1)
            continue
        if section_end_match:
            current_section = None
            continue
        if line.startswith('#'):
            continue

        domain_match = re.match(r'^0\.0\.0\.0\s+(\S+)$', line)

        if (domain_match):
            domains.append({
                'domain': domain_match.group(1),
                'ip' : "0.0.0.0",
                'category' : current_section or 'Uncategorized'
            })
    return domains

# Get file descriptor
def catch_content(path,mode):
    file = open(path, mode)
    return file

# Search for the domain on folder for the domain.
def search_for_string(text,path):
    domain_exist = False
    domain_on_file = False
    file = catch_content(path,"r")
    contents = file.read().split('\n')
    file.close()
    for line in contents:
        match = re.match(r"^" + text + r"\tIN*",line)
        if match:
            domain_exist = True
            continue
        if domain_exist:
            domain_on_file = True
            break
    return domain_on_file

# Add domain on the file.
def add_block(domain,path,type):
    file = catch_content(path,"a")
    string_domain = "\n" + domain + "\tIN\tA\t0.0.0.0\t#" + type
    file.write(string_domain)
    file.close()

            

