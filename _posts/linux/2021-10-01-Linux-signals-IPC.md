---
layout: post
title: "Linux Signals"
date: 2017-01-01
categories: ['Linux']
excerpt_separator: <!--more-->
---


- Signals are also referred to as software interrupts. They are mechanism to notify a process of some event and interrupt their execution flow.

- Kernel sends signals to process for:
    - hardware exception: sigsegv, divide-by-zero
    - User issueing ctrl-c or ctrl-z
    - Software event occured: input became avialable on FD, child of process terminated etc.

    