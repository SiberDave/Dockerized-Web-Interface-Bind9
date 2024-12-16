#! /bin/python3
import sys
from helper import list_domain_block

path = r"/etc/bind/db.blocked.rpz"

list_domain_block(path)