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
        checkfile = re.match('^0\.0\.0\.0.',line)
        section_match = re.match(r'^#<(\w.+)>$',line)
        section_end_match = re.match(r'#</(\w.+)>$',line)

        if checkfile:
            right_file = True

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
    
    if not right_file:
        return False
    return domains

# Refresh Bind Config
def bind_refresh_option():
    var = subprocess.run(["/usr/sbin/rndc","reload"],stdout=subprocess.DEVNULL)

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
        if (re.match(r"\*.",text)):
            match = re.match(r"^\*." + text + r"\tIN\t" + type + "\t",line)
        else:
            match = re.match(r"^" + text + r"\tIN\t" + type + "\t",line)
        if match:
            domain_exist = True
            continue
        if domain_exist:
            domain_on_file = True
            break
    return domain_on_file

# Add domain on the bind config file.
def add_domain_block(domain,path,type):
    ip_address="0.0.0.0"
    file = catch_content(path,"a")
    if type == "AAAA":
        ip_address="::"
    elif type == "HTTPS":
        type = "A"
    string_domain = domain + "\tIN\t" + type + "\t" + ip_address + "\n"
    is_www = re.match(r"^www",domain)
    file.write(string_domain)
    if is_www == None:
        star_string_domain = "*." + domain + "\tIN\t" + type + "\t" + ip_address + "\n"
        file.write(star_string_domain)
    file.close()
    bind_refresh_option()

# List domain on the bind config file.
def list_domain_block(path):
    file = catch_content(path,"r")
    contents = file.read().split('\n')
    for line in contents:
        match = re.match(r"\w",line)
        match_star = re.match(r"^\*.\w",line)
        if match or match_star:
            temp_text = line.split('\t')
            try:
                print(str(temp_text[0])+","+str(temp_text[2]))
            except:
                continue
    bind_refresh_option()

# Delete domain on the bind config file
def delete_domain_block(domain,path,type):
    file = catch_content(path,"r")
    lines = file.readlines()
    new_array = []
    for line in lines:
        if (re.match(r"\*",domain)):
            match = re.match(r"^\*." + str(domain) + r"\tIN\t" + type + "\t",line)
        else:
            match = re.match(r"^" + str(domain) + r"\tIN\t" + type + "\t",line)
        if match == None:
            new_array.append(line)
    file = catch_content(path, "w")
    file.writelines(new_array)
    file.close()
    bind_refresh_option()
    print("Domain " + domain + " Successfully Deleted!")
    