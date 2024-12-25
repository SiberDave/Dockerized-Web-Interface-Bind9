#! /bin/bash

systemctl stop systemd-resolved && systemctl disable systemd-resolved
systemctl start named node_api 
/home/webScript/Blocked_Domain_add.py doubleclick.net A