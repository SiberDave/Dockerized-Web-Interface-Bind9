#! /bin/python3

import sys
from helper import delete_domain_block, search_for_string

domain = sys.argv[1]
type = sys.argv[2]
path = "/etc/bind/db.blocked.rpz"

status = search_for_string(domain,path,type)

if status:
    delete_domain_block(domain,path,type)
else:
    print("Domain " + domain + " with type of " + type + " aren't on block list")