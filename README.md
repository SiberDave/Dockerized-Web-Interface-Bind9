# Web Interface Bind9

Web Interface for Bind9 which allow user to build bind9 dns server and the web interface for it and supporting on some feature such as:
- Domain Block using RPZ.
- Client Whitelisting (Default deny all).
- Dns Logging.
- Custom Domain.
- Accept both Dns-over-Https and DNS Connection.


# Web Interface Bind9 Components 
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


## Ports Used
- 3000 (Backend node.js)
- 8080 (Frontend)
- 5053 (dnscrypt-proxy)
- 8443 (DoH Bind9)
- 53/UDP (Bind9)

## How to Install

1. On Dockerfile.backend on line 38, Change the ip 127.0.0.1 to your public facing ip / ip address you want to use as DoH dns server.

2. On Dockerfile.frontend on line 15, Change the localhost to Backend ip which reachable from public or your device.

3. Run `docker-compose build --no-cache` to build the image.

4. Run `docker-compose -p "bind9-interface" up -d`.

5. Add ip to the Allowed Client menu on website to allow device to connect to dns server.

## Troubleshoot
Q: Issue on network overlapping <br/>
A: Please change the ip subnet of docker network on docker-compose.yaml also the ip for each service and additional host for dns_backend service
