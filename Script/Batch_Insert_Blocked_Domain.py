#! /bin/python3

import sys, re
from helper import parse_hosts_file, search_for_string, add_domain_block, catch_content, bind_refresh_option

#host_url = 'https://someonewhocares.org/hosts/zero/hosts'
host_url = sys.argv[1]
type = sys.argv[2]
path = r"/etc/bind/db.blocked.rpz"

def add_domain(domain,type,file):
    string_domain = domain + "\tIN\t" + type + "\t0.0.0.0\n"
    is_www = re.match(r"^www",domain)
    file.write(string_domain)
    if is_www == None:
        star_string_domain = "*." + domain + "\tIN\t" + type + "\t0.0.0.0\n"
        file.write(star_string_domain)

parsed_hosts = parse_hosts_file(host_url)

if not parsed_hosts:
    print("file bukan file host")
elif parsed_hosts == "Error1":
    print("Domain tidak valid!")
else:
    success = True

    count_sukses = 0

    file = catch_content(path,"a")

    for host in parsed_hosts:
        if host['ip'] == '0.0.0.0':
            status = search_for_string(host["domain"],path,type)
            if status == False:
                add_domain(host["domain"],type,file)
                count_sukses+=1
            else:
                continue
        else:
            print("Host isn't 0.0.0.0")
            success = False
            break
    file.close()
    if success:
        print(str(count_sukses) + " domain sudah sukses ditambahkan")
        bind_refresh_option()
    else:
        print(str(count_sukses) + " domain sudah sukses ditambahkan, namun ada beberapa kesalahan")