#!/bin/bash
path=/etc/bind/db.custom.dns
domain=$1
address=$2

sh -c "sed -i '/^\b$domain\b.*\b$address\b/d' $path"

file_contents=$(cat $path)

if [[ ! $file_contents =~ "$pattern\tIN\tA\t$address" ]]; then
	echo "domain $1 have been deleted"
fi

rndc reload > /dev/null