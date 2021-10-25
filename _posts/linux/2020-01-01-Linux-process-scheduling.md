---
layout: post
title: "Linux Processes - scheduling"
date: 2017-01-01
categories: ['Linux']
excerpt_separator: <!--more-->
---

- Scheduler is the component of kernel which selects which process to run next thus maximizing processor usage providing illusion of multiple processes are executing together thus multi-tasking. Multitasking systems are of two types:

1. Pre-emptive: Linux
2. Co-operative: Old systems(Win 3.1 etc)

- Linux employs pre-emptive scheduling where the scheduler decides when to stop and run as process.

# Classes of Process:
1. Interactive Processes:These spend most of time interacting with user thus waiting for user I/O. shells, text editor etc.
2. Batch Processes: These execute in background. Compilers, database search engines, scientific
3. Real-time processes: These need guaranteed response time. Multimedia apps (video player etc):
    1. hard real time system
    2. soft real time system

# Types of processes:
The classes of processes can fall into two types:
1. CPU Bound
    - Processes which consume all of their available time-slices are called as CPU bound.
    - These processes crave for largest timeslices
2. IO-Bound
    - Processes which spend more time blocked waiting for some resource are called as I/O bound.
    - Do not necessarily need large timeslices.
    - I/O bound application do need prioritized attention from processor as when they get unblocked they would like to execute fast.
    - In CFS scheduler, vruntime of these processes will be small as their burst time is small. Hence they are on the left side of the tree. This way they get run often.
    - 


# Traditional Unix Sheduler

- has 32 run queues which work in round robin with 


# CFS

- It has five classes of process:
    1. stop: Highest priority. They can pre-emp anyone and can be pre-emptied by anyone. ftrace, clocks.
    2. Deadline: Uses SCHED_DEADLINE policy for period realtime tasks.
    3. realtime: Uses SCHED_FIFO and SCHED_RR. Used for POSIX realtime tasks such as IRQ Threads with priority values from 0-99
    4. CFS: SCHED_NORMAL, SCHED_BATCH, SCHED_ISO, SCHED_IDLEPRO. Used for userspace processes. such as bash. Priority values used: 
                100-139 
                nice values of -20 to +19
                this maps to 0-39

                priority = 20 + nice

                higher the priority number lowe is priority given by processor.

    5. idle: Lower priority. No policy. when nothing to run.


    - CFS uses ideal fair scheduling: The processor time is divided equally amongst the running processes. Thus if you have n runnable processes, then each will get 1/n of processor time.

    - vruntime: Amount of time a process has run and served. This acts as the index for the tree or rather node.val in red black tree implementation of CFS.

    - Tasks with lowest vruntime are on left side of tree. These need the the CPU most. The task on right side of tree are with highest vruntime and needs cpu the least.

# For new processes:
    - CFS keeps track of min vruntime, and new task gets that value.
    - Thus, new process is executed immediately.
    - when context switch or interupt happen
        - the processes vruntime += exec_duration * (weightage based on the nice value)
            Thus, higher the nice, higher the weightage and higher the vruntime, and the task will be on the right side of the tree.
        - choose the process with min_vruntime.
        - calculate its Dynamic TimeSlice.
        - repeat.


    When does contect switch happens?:
        - when there is a task with higher priority that other.
        - When there is a task with low vruntime than current

            
    - CPU Bound and I/O bound process handling
            - Text editor: Low vruntime because it runs less often.
            - Video editor: High vruntime. Whernever it wakes up, it pre-empts the text editor.


# How to check priority of process
```
root@vinlok-ThinkPad-T400:~# ps -l -q $$
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
4 S     0  262843  262842  0  80   0 -  2659 do_wai pts/1    00:00:00 bash
```

- Here priority is 80. Higher the number lower the priority. The nice value is 0. Hence the effective priority is 80.

- Below show the effect of renicing

```
root@vinlok-ThinkPad-T400:~# renice 10 $$
262843 (process ID) old priority 0, new priority 10
root@vinlok-ThinkPad-T400:~# ps -l -q $$
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
4 S     0  262843  262842  0  90  10 -  2659 do_wai pts/1    00:00:00 bash
root@vinlok-ThinkPad-T400:~# renice -10 $$
262843 (process ID) old priority 10, new priority -10
root@vinlok-ThinkPad-T400:~# ps -l -q $$
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
4 S     0  262843  262842  0  70 -10 -  2659 do_wai pts/1    00:00:00 bash
```

- Again, lower the nice will yeild lower priority number thus means higher priority.

- Child process inherits the nice of parent.

- To run a program with new nice value prepend it with nice <newval> <command>

```
root@vinlok-ThinkPad-T400:~# schedtool $$
PID 262843: PRIO   0, POLICY N: SCHED_NORMAL  , NICE -10, AFFINITY 0x3
```
- Here you can see that the process can run on binary equivalent of 3 = 11 means it can run on first and second processor.

```
root@vinlok-ThinkPad-T400:~# schedtool -r
N: SCHED_NORMAL  : prio_min 0, prio_max 0
F: SCHED_FIFO    : prio_min 1, prio_max 99
R: SCHED_RR      : prio_min 1, prio_max 99
B: SCHED_BATCH   : prio_min 0, prio_max 0
I: SCHED_ISO     : policy not implemented
D: SCHED_IDLEPRIO: prio_min 0, prio_max 0
```

- This lists the scheduling policies available for processes.
- SCHED_FIFO and RR are for realtime processes (I/O threads). Process running with SCHED_FIFO cannot be pre-emptied but they yield themselves using the yield syscall.
- SCHED_RR realtime process get small timeslices.
- You can use schedtool to change any of the above values.
-

# System calls

- nice() -> to get and set nice of process itself. Cannot be used to change for other priority[]

- getpriority(which, who) and setpriority(which, who, prio):
    which can be: PRIO_PROCESS, PRIO_PGRP, prio_USER (realuserid)


- sched_yield() -> caused the process to relinquish the CPU. Done by real time processes in FIFO policy

- sched_getcpu() , sched_getaffinity() , sched_setaffinity()

# Processor / CPU affinity
- On a System with multiple CPU's a task can get scheduled on any of the CPU. When a process get scheduled from one CPU to other, the cache of the CPU needs to be moved as well. Thus, the old cache needs to be invalidated and new one needs to be set.
- Processor affinity can be used to run process on same CPU:
    - soft affinity
    - hard affinity

# Checking processes priority

- top will show the processes priority and nice value
- For realtime processes:
    - the value will be either negative or rt. Use schedtool <pid> to see the real value
    
# References

- https://www.youtube.com/watch?v=scfDOof9pww
