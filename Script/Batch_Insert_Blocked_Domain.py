#! /bin/python3

import sys
from helper import parse_hosts_file, search_for_string, add_block

#host_url = 'https://someonewhocares.org/hosts/zero/hosts'
host_url = sys.argv[1]
path = r"/etc/bind/db.blocked.rpz"

parsed_hosts = parse_hosts_file(host_url)

count_sukses = 0

for host in parsed_hosts:
    if host['ip'] == '0.0.0.0':
        status = search_for_string(host["domain"],path)
        if status == False:
            add_block(host["domain"],path,host["category"])
            count_sukses+=1
    else:
        print("Host isn't 0.0.0.0")

print(str(count_sukses) + " domain sudah sukses ditambahkan")