#! /bin/python3

import sys
from helper import parse_hosts_file, search_for_string, add_domain_block

#host_url = 'https://someonewhocares.org/hosts/zero/hosts'
host_url = sys.argv[1]
type = sys.argv[2]
path = r"/etc/bind/db.blocked.rpz"

parsed_hosts = parse_hosts_file(host_url)

if not parsed_hosts:
    print("file bukan file host")
elif parsed_hosts == "Error1":
    print("Domain tidak valid!")
else:
    success = True

    count_sukses = 0

    for host in parsed_hosts:
        if host['ip'] == '0.0.0.0':
            status = search_for_string(host["domain"],path,type)
            if status == False:
                add_domain_block(host["domain"],path,type,host["category"])
                count_sukses+=1
        else:
            print("Host isn't 0.0.0.0")
            break

    if success:
        print(str(count_sukses) + " domain sudah sukses ditambahkan")