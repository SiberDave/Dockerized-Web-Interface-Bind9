#! /bin/python3

import sys
from helper import search_for_string, add_block

domain = sys.argv[1]
category = sys.argv[2]
path = r"/etc/bind/db.blocked.rpz"

status = search_for_string(domain,path)
if status == False:
    add_block(domain,path,category)
    print("Domain " + domain + " is successfully blocked!")
else:
    print("Domain is already blocked!")