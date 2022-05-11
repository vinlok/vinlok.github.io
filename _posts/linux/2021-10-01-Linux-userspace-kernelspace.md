---
layout: post
title: "Linux Userspace and Kernelspace"
date: 2017-01-01
categories: ['Linux']
excerpt_separator: <!--more-->
version: 1
---


Processes are running instance of programs. When a process is executing some code not needing the kernels interuption, it is running in userspace accessing the userspace of the process memory map. When the process needs kernel to do some work example accessing shared resources, it enters in kernel space.

When running in user space, it will only use user CPU time, when running in kernel space, it will use the system CPU time.


# User space program example

Let's take a look at the following C program:

```

root@vinlok-ThinkPad-T400:~# cat userspace.c
#include<stdio.h>
#include<string.h>

void main(){

	char name[10]="vinayak"; //local initialized var, store in stack
	int i;
	for (i=0;i<100000000;i++){
	strlen(name); //string manipulation function handled by glibc not needing kernel help.
	}

}
```

Here the strlen function would not need kernel to access resources or perform any operation for the program. Hence, the systime used would minimal and most of the time would be spend in usertime:

```
root@vinlok-ThinkPad-T400:~# gcc userspace.c -static
root@vinlok-ThinkPad-T400:~#
root@vinlok-ThinkPad-T400:~# time ./a.out

real	0m0.287s
user	0m0.282s
sys	0m0.004s
root@vinlok-ThinkPad-T400:~# time ./a.out

real	0m0.286s
user	0m0.281s
sys	0m0.004s
```

This is also evident in from system call trace using strace:

```
root@vinlok-ThinkPad-T400:~# strace ./a.out
execve("./a.out", ["./a.out"], 0x7ffd2205c370 /* 15 vars */) = 0
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffc9fba4f70) = -1 EINVAL (Invalid argument)
brk(NULL)                               = 0x15f6000
brk(0x15f71c0)                          = 0x15f71c0
arch_prctl(ARCH_SET_FS, 0x15f6880)      = 0
uname({sysname="Linux", nodename="vinlok-ThinkPad-T400", ...}) = 0
readlink("/proc/self/exe", "/root/a.out", 4096) = 11
brk(0x16181c0)                          = 0x16181c0
brk(0x1619000)                          = 0x1619000
mprotect(0x4bd000, 12288, PROT_READ)    = 0
exit_group(0)                           = ?
+++ exited with 0 +++

```

Here you can see that after the initial syscalls, there are no systemcalls requesting kernel to do anyoperations.


# Kernel Space, Kernel Mode system time

Lets consider the following code:

```
root@vinlok-ThinkPad-T400:~# cat kernelspace.c
#include<stdio.h>
#include<stdlib.h>

void main(){
	int i;
	for (i=0;i<10000;i++){
	int *pointer = malloc(4192);
    	*pointer=1;
	//free(pointer);
	//printf("a");
	}
}
```
Explanation:

Here, we are using malloc to allocate 4192 bytes of memory. Malloc return a void * pointer. This pointer is essentially not of any type and can be type cast into anytime. In this case we are changing it to integer type.

Next, to this pointer, we store integer value 1


```
root@vinlok-ThinkPad-T400:~# gcc kernelspace.c -static
root@vinlok-ThinkPad-T400:~# time ./a.out

real	0m0.045s
user	0m0.000s
sys	0m0.045s
root@vinlok-ThinkPad-T400:~# strace ./a.out
execve("./a.out", ["./a.out"], 0x7fffc45908b0 /* 15 vars */) = 0
arch_prctl(0x3001 /* ARCH_??? */, 0x7fff602b2610) = -1 EINVAL (Invalid argument)
brk(NULL)                               = 0x1375000
brk(0x13761c0)                          = 0x13761c0
arch_prctl(ARCH_SET_FS, 0x1375880)      = 0
uname({sysname="Linux", nodename="vinlok-ThinkPad-T400", ...}) = 0
readlink("/proc/self/exe", "/root/a.out", 4096) = 11
brk(0x13971c0)                          = 0x13971c0
brk(0x1398000)                          = 0x1398000
mprotect(0x4bd000, 12288, PROT_READ)    = 0
brk(0x13b9000)                          = 0x13b9000
brk(0x13da000)                          = 0x13da000
brk(0x13fb000)                          = 0x13fb000
brk(0x141c000)                          = 0x141c000
brk(0x143d000)                          = 0x143d000
brk(0x145f000)                          = 0x145f000
brk(0x1480000)                          = 0x1480000
brk(0x14a1000)                          = 0x14a1000
brk(0x14c2000)                          = 0x14c2000
brk(0x14e3000)                          = 0x14e3000
brk(0x1504000)                          = 0x1504000

```

As you can see, malloc would make brk() system call everytime. This is to change the breakpoint in the heap to allocate memory. This needs kernel to perform the operation hence the system CPU time is used more.


# References
- https://www.geeksforgeeks.org/decoding-information-from-the-strace-output/
- https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/

- https://tldp.org/LDP/lkmpg/2.6/lkmpg.pdf