version: 1

# What happens when you CURL a URL.

- Curl would parse the URL into:
    - protocol
    - Resource

## For the resource
- Do a gethostbyname which will check /etc/hosts
- if found, it is returned.

- If not found, then it will find the IP of the DNS server in the /etc/resolv.conf
    ```
    In case of linux, the systemd-resolve is used which is set to 127.0.0.53 address. This would cache the DNS entry.
    ``` 

Contacting DNS Server

At this point you have the IP address of the DNS server. Now you need to make a DNS query.

For that you need to find the MAC address to which you have to send the frame
(Remember that the frame works on the data layer, hence, you need the dest IP to MAC ddress even for DNS )

Finding the MAC address for the traget IP (DNS server IP in this case)

- First, the ARP cache is checked to see if you have IP - MAC mapping

```
root@vinlok-ThinkPad-T400:~# arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.0.15             ether   8c:85:90:07:f7:7f   C                     wlp3s0
_gateway                 ether   6c:cd:d6:fe:b7:4a   C                     wlp3s0
```

- If found then MAC is returned.

- If not, then it needs to do a ARP brodcast. But in order to find the interface on which it needs to do broadcast, route table is looked up to see which interface has subnet associated with out destination IP (DNS server IP in this case)

- Now that you have the MAC address of the interface which has route to the DNS, ARP broadcast is done on that interface FF:FF:FF:FF:FF:FF (48 bit or 12 hex chars)

Now the interface or computer, can be connected to:

1.SWITCH:

1. Switch will check the local MAC table to see which port is mapped to the MAC address.
    if found, then send the ARP request to that PORT which will respond with its IP

    if not found, then the brodcast is send to all the ports. If the server is connected to the swithch then it replies.

    If it is a router, then it will respond.

11. Finally, the network has the IP address of the DNS server.

12. It will now establish a socket to port 53 with UDP protocol. Here the source port will be ephermal port.

13. The DNS request will be sent. If the response is too large (more than 512 Bytes), then TCP is used.