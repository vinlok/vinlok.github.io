version: 1

# vmstat


```
root@vinlok-ThinkPad-T400:~# vmstat -Sm 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      1    188    129   2896    0    0    42    65  127  159  1  0 98  0  0
 0  0      1    188    129   2896    0    0     0     0  207  213  0  1 100  0  0
 0  0      1    188    129   2896    0    0     0     0  293  270  0  0 99  0  0
 0  0      1    188    129   2896    0    0     0     0  212  265  0  0 100  0  0
 0  0      1    188    129   2896    0    0     0     0  175  203  0  0 100  0  0  

 ```


 Procs:
r: The number of runnable processes (running or waiting for run time).
b: The number of processes in uninterruptible sleep.

 Memory:
 swpd: Amount of swap used (total)
 free: Free available memory (free list)
 buff: Memory in buffer cache (This is meta data for the cache)
 cache: Memory in page cache.
 si: memory swapped in from disk to RAM (disk to RAM)
 so: memory swapped out to disk from RAM (RAM to disk)




# iostat

- iostat -sxm -p ALL 2 /dev/sda

```
root@vinlok-ThinkPad-T400:~# iostat -sxm 2 /dev/sda
Linux 5.11.0-38-generic (vinlok-ThinkPad-T400) 	11/25/2021 	_x86_64_	(2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.68    0.38    0.39    0.07    0.00   98.49

Device             tps      MB/s    rqm/s   await  areq-sz  aqu-sz  %util
sda               3.40     20.65     4.14    1.37  6227.65    0.01   0.32


avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.75    0.00    0.75    0.00    0.00   98.51

Device             tps      MB/s    rqm/s   await  areq-sz  aqu-sz  %util
sda               0.00      0.00     0.00    0.00     0.00    0.00   0.00

```

- tps: Transactions issued per second (IOPS)
- kB/s: Kbytes per second
- rqm/s: Requests queued and merged per second
- await: Average I/O response time, including time queued in the OS and
    the I/O response time of the device (ms)
- aqu-sz: Average number of requests both waiting in the driver request
- queue and active on the device
- areq-sz: Average request size in Kbytes
- %util: Percent of time the device was busy processing I/O requests

await: Most important.
%util: Indication of saturation.
rqm/s: Non zero show requests were mereged before being written indicating sequential I/O.

areq-sz: This is average request size after merging. If it is smaller than 8kb, generally it is indication of random IO

- iostat -xm 1

```

root@vinlok-ThinkPad-T400:~# iostat -xm 2 /dev/sda
Linux 5.11.0-38-generic (vinlok-ThinkPad-T400) 	11/25/2021 	_x86_64_	(2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.66    0.36    0.37    0.06    0.00   98.55

Device            r/s     rMB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wMB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dMB/s   drqm/s  %drqm d_await dareq-sz  aqu-sz  %util
sda              1.27      0.06     0.37  22.80    1.00    49.38    1.45      0.10     3.57  71.06    1.82    69.61    0.52     19.46     0.00   0.00    1.02 38626.50    0.00   0.31
```

- pidstat 1
Prints rolling output only for process which are active.
```


root@vinlok-ThinkPad-T400:~# pidstat -d
Linux 5.11.0-38-generic (vinlok-ThinkPad-T400) 	11/25/2021 	_x86_64_	(2 CPU)

05:56:51 PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s iodelay  Command
05:56:51 PM     0         1     23.65     45.20      1.36      21  systemd
05:56:51 PM     0       209      0.00      1.19      0.00    1084  jbd2/sda5-8
05:56:51 PM     0       250      0.05      2.06      0.00      11  systemd-journal
05:56:51 PM     0       275      3.56      0.00      0.00       1  systemd-udevd
05:56:51 PM     0       293      0.00      0.00      0.00       0  loop0

```



# top

1. the TIME colums shows total CPU time used since it is running.
2. %cpu shows the utilization of CPU. This can be 200% for multithreaded app.




# Troubleshooting a slow process

- You get a complaint that a process is slow.

Steps
1. ps -aux | grep find -> to see if the process is alive and get PID
2. top -cbp 1234
    - Here check for TIME and %CPU field
3. One you have the PIC, then you can cat /proc/pid/wchan. wchan is the part of kernel code the process is executing/waiting.

4. Now, you can do a cat on  /proc/pid/status and check:
    - State : (DIRSTtZ)
    - Voluntary CTX switches
    - nonVoluntary CTX switches.

5. Now if the strace is getting stuck, you can 
cat /proc/pid/syscall 
to see the syscall the process is executing.

6. Here you can see the syscall number the process is stuck executing.

7. Then, you can also run cat /prod/pid/stack to see the stack of the process.
Hopefully here you can see the call where the process is stuck.

Remediation:
1. Either do a HUP signal
2. Kill -9



# Trobleshooting Network issues

- ping
1. Does ICMP echo request to destination. The reply to this is ICMP reply.
2. 


- traceroute:

1. Sends icmp packets with ttl as 1 all the way up to the destination.
2. 

- nc:

nc -zv google.com 80

- 
