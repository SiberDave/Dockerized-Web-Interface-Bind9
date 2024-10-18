# dockerize-bind9-rpz-monitor-backend
Bind9 RPZ monitor made with 
- vue.js
- express.js
- node.js
- bind9
- dnscrpyt-proxy
- MongoDB
- Docker
- Docker-compose

## Things to Install
- docker
- docker-compose

## OS supported

- Ubuntu 20.04 or Below

## How to Install

1. Run `docker-compose -p "bind9-interface" up -d`

## Troubleshoot
Q: Issue on network
A: change the ip subnet of docker network on docker-compose.yaml also the ip of each service and additional host for dns_backend service
