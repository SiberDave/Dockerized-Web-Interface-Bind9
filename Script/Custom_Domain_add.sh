#!/bin/bash

record="A"
domain=$1
address=$2

function add_domain()
{
    domain=$2

    address=$3

    if sed -n "/$domain\\tIN\\t$record\\t$address/p" $1 | grep -q .; then
        echo "failed"
    else
        sh -c "echo '$domain\tIN\t$record\t$address' >> $1"
        echo "success"
    fi
}

domain_status=$(add_domain /etc/bind/db.custom.dns $domain $address)

if [ "$domain_status" == "success" ]; then
    echo "Domain Successfully Added"
elif [ "$domain_status" == "failed" ]; then 
    echo "Domain Already Registered."
else
    echo "$domain_status"
fi

rndc reload > /dev/null