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

2. Run `docker-compose build --no-cache` to build the image.

3. Run `docker-compose -p "bind9-interface" up -d`.

4. Run `docker exec -it interface-bind9-backend bash` to go into inside of container.

5. Run `/home/webScript/run_service.sh` to run service of backend app and bind9.

6. Add ip to the Allowed Client menu on website to allow device to connect to dns server.

## Troubleshoot
Q: Issue on network <br/>
A: change the ip subnet of docker network on docker-compose.yaml also the ip of each service and additional host for dns_backend service
