---
layout: post
title: "Linux Sockets"
date: 2017-3-25
categories: ['Linux']
excerpt_separator: <!--more-->
---

Socket are essentially two ways pipe for communication.

# Domains of Socket:
    - Unix Domain socket: AF_UNIX
    - Internet Domain Sockets: AF_INET

# Type of sockets:
    - Stream
    - Datagram

# Unix domain sockets

- These are just FIFO(Named pipes) two ways.
- All the communication happens over socket interface (bind, send, receive) rather than file interface (open, read, write)

Server:

- create a new socket s using socket() in AF_UNIX domain of type stream.
- Then create a struct of type sockaddre_un lets says local which contains the path of socket (/tmp/server_socket)
- Then bind the socket to the struct using bind(s,local)
- now start listening on the socket using listen(s,max_connections). This creates a passive socket which is where we have switched the socket to accept connection mode.

- Now accept a new connection using s2 = accept(s,new_struct). The passive one is still listening but here you connect to client.
- Now go in while loop
    - recv(s2,buff)
    - send(s2,buff)
- close(s2)

client:
- Create a new socket in AF_UNIX domain of type stream.
- create a struct of type struct_un binding to /tmp/server_socket. Lets call it remote.
- Connect socket s to remote: connect(s,remote)
- now go in while loop:
    - send
    - recev


## Socketpair:

- Here the sockets are created for bi-directional communication between parent and child:
- steps:
    - create array sv[2]
    - create a socketpair using socketpair(AF_UNIX,DG_STREAM,sv)
    - pid=fork()
        if pid=0:
            //in client
            read(sv[1])
            write(sv[1])
        else:
        //parent
            read(sv[0])
            write(sv[0])

- Here as the child has the copy of parent fd, you do not need to create a temp file.


# Internet Domain Sockets
- Port numbers: 0-1023 reserved
by IANA and are privilege
- 49152 to 65535: dynamic or ephernal.
- UDP
- TCP
    - connection oriented
    - flow control
    - retranmission
    - sequencing
    - congestion control