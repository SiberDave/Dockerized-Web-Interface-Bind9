# dockerize-bind9-rpz-monitor-backend
Bind9 RPZ monitor made with 
- Vue.js
- Express.js
- Node.js
- Bind9 (development)
- Dnscrpyt-proxy
- MongoDB
- Docker
- Docker-compose

## Things to Install
- docker
- docker-compose

## OS Tested

- Ubuntu 20.04 or Below

## Ports Used
- 3000 (Backend node.js)
- 8080 (Frontend)
- 10053 (dnscrypt-proxy)
- 8443 (DoH Bind9)
- 53/UDP (Bind9)

## How to Install

1. On Dockerfile.backend on line 38, Change the ip 127.0.0.1 to your public facing ip / ip address you want to use as DoH dns server.

2. On Dockerfile.frontend on line 15, Change the localhost to Backend ip which reachable from public or your device.

3. Run `docker-compose build --no-cache` to build the image.

4. Run `docker-compose -p "bind9-interface" up -d`.

5. Add ip to the Allowed Client menu on website to allow device to connect to dns server.

## Troubleshoot
Q: Issue on network <br/>
A: change the ip subnet of docker network on docker-compose.yaml also the ip of each service and additional host for dns_backend service
