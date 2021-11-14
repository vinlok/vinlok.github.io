---
layout: post
title: "Common Latency Numbers"
date: 2017-3-25
categories: ['Linux']
excerpt_separator: <!--more-->
---



<!--more-->
- processor cycle               : 1/3 ns
- Accessing memory              : 100 ns 
- context switching             : 1.2 micro seconds or 1.2 us
- reading 1 MB from RAM         : .25 ms = 250 us
- round trip in same DS         : .5 ms = 500 us
- reading 1 MB from SSD         : 1 ms
- Disk Seek                               : 10 ms
- Transfer 1 MB over 1 GB network         : 10 ms
    Math:
        1 GB/s = 1 x 10^9 bit / s = 10^9/10 Bytes / sec = 10^8 Bytes = 10^2 MB/second
        Thus for 1 MB time needed = 1/100 = .01 s = 10 ms
        (we rounded off byte to 10)

- 1 MB seq from mag disk        : 20 ms
- Inter-continental round trip  : 150 ms


1 Disk seek ~= 25 x 10^6 million times of a processor cycle!


# Data transfers

1 MB over 1 GBps = 10 ms
100 MB           = 1 s
1 GB             = 10 s




# References

- https://people.orie.cornell.edu/bdg79/ORIE6125/lecture8.html