#! /bin/python3

import sys
from helper import search_for_string, add_domain_block

domain = sys.argv[1]
category = sys.argv[2]
type = sys.argv[3]
path = "/etc/bind/db.blocked.rpz"

status = search_for_string(domain,path,type)
if status == False:
    add_domain_block(domain,path,type,category)
    print("Domain " + domain + " is successfully blocked!")
else:
    print("Domain is already blocked!")