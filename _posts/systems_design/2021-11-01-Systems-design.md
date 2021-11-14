Systems design misc

# Proxies

## Forward proxies:
    - proxy is often used here.
    - It is a server that sits between client and server and acts on behalf of the clients.
    - Communication:
        - client to proxy to server
        - server to proxy to client

    Both side communication goes via proxy.

    - It essentially masks the identity of the client (x-forward-ip)
    - VPN can be though of a forward proxy.

## Reverse Proxy

    - They act on behalf of server.
    - Communication:
        - client to proxy to server
        - server to proxy to client

    - This is what is used in loadbalancer. 
    - The AWS Loadbalancers are reverse proxy servers.
    - You can add rules, log requests coming to your servers.

# Load Balancers
- 