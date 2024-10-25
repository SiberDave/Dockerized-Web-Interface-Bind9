#!/bin/bash

filename="/var/log/bind/cache_dump.db"

# if [ ! -e "$filename" ]; then 
# 	rndc dumpdb -cache
# fi

# disabled for testing
rndc dumpdb -cache

while read line; do
    echo "$line" | sed -e '/^;/d' | sed -e '/^$DATE/d' | awk 'NF <= 4 && NF >= 3 {print}' | awk '$2 !~ /IN|RSIG/ && $2 !~ /^[0-9]{14}$/ {print}' | awk '$4 !~ /NXRRSET/ {print}' | awk '$3 !~ /#/ {print}'
done < $filename
