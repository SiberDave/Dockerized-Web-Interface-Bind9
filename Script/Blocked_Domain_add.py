#! /bin/python3

import sys
from helper import search_for_string, add_block

domain = sys.argv[1]
path = r"./try_bind_conf"

status = search_for_string(domain,path)
if status == False:
    add_block(domain,path,"Uncategorized")
    print("Domain " + domain + " is successfully blocked!")
else:
    print("Domain is already blocked!")