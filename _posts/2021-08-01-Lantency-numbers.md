---
layout: post
title: "Common Latency Numbers"
date: 2017-3-25
categories: ['Linux']
excerpt_separator: <!--more-->
---



<!--more-->
- processor cycle       : 1/3 ns
- Accessing memory      : 100 ns 
- context switching     : 1.2 micro seconds or 1.2 us
- round trip in same DS : .5 ms 
- 1 MB seq read SSD     : 1 ms
- Disk Seek             : 10 ms
- 1 MB seq from mag disk: 20 ms


1 Disk seek ~= 25 x 10^6 million times of a processor cycle!


# References

- https://people.orie.cornell.edu/bdg79/ORIE6125/lecture8.html