#! /bin/python3

import requests
import re
import subprocess

# Get the hosts file from network and parse it to csv
def parse_hosts_file(url):
    domains = []
    current_section = None
    right_file = False

    try:
         response = requests.get(url)
    except:
        return "Error1"


    response.raise_for_status()

    lines = response.text.split('\n')

    for line in lines:
        checkfile = re.match('^0.0.0.0.',line)
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

        if checkfile:
            right_file = True
            continue
        else:
            break
    
    if not right_file:
        return False
    return domains

# Refresh Bind Config
def bind_refresh_option():
    subprocess.run(["rndc", "reload > /dev/null"])

# Get file descriptor
def catch_content(path,mode):
    file = open(path, mode)
    return file

# Search for the domain on folder for the domain.
def search_for_string(text,path,type):
    domain_exist = False
    domain_on_file = False
    file = catch_content(path,"r")
    contents = file.read().split('\n')
    file.close()
    for line in contents:
        match = re.match(r"^" + text + r"\tIN\t" + type + "\t",line)
        if match:
            domain_exist = True
            continue
        if domain_exist:
            domain_on_file = True
            break
    return domain_on_file

# Add domain on the bind config file.
def add_domain_block(domain,path,type,category):
    file = catch_content(path,"a")
    string_domain = domain + "\tIN\t" + type + "\t0.0.0.0\t#" + category + "\n"
    file.write(string_domain)
    file.close()
    bind_refresh_option()

# List domain on the bind config file.
def list_domain_block(path):
    file = catch_content(path,"r")
    contents = file.read().split('\n')
    for line in contents:
        match = re.match(r"\w",line)
        if match:
            temp_text = line.split('\t')
            print(temp_text[0]+","+temp_text[2]+","+temp_text[4].split('#')[1])
    bind_refresh_option()

# Delete domain on the bind config file
def delete_domain_block(domain,path,type):
    file = catch_content(path,"r")
    lines = file.readlines()
    new_array = []
    for line in lines:
        match = re.match(r"^" + domain + r"\tIN\t" + type + "\t",line)
        if match == None:
            new_array.append(line)
    file = catch_content(path, "w")
    file.writelines(new_array)
    file.close()
    bind_refresh_option()
    print("Domain " + domain + " Successfully Deleted!")
    