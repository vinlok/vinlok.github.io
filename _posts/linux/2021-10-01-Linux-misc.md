---
layout: post
title: "Linux Misc"
date: 2017-01-01
categories: ['Linux']
excerpt_separator: <!--more-->
version: 1
---

# Users and Groups, Process UID, SetUID

- Primary purpose of UID is to determine the ownership of resources.
- /etc/passwd format:
vinlok:x:1000:1000:vinlok,,,:/home/vinlok:/bin/bash

Loginname:enc_passwd:UID:GID:Comment:Home_dir:Login_shell

- /etc/shadow stores the encrypted passwords only root has access to this:
vinlok:$6$ts7Io8UaJO50x6eo$iM0mwR.z3tUS5lU1G3Zq46VX/4OvtLizGOwnng9qFEkFqaGNcQ.69ZhilTQOicJ/yBQqWZV.aBNGXFkO3XvlR0:18812:0:99999:7:::
- /etc/groups stores the group info of Linux systems:
vinlok:x:1000:
sambashare:x:132:vinlok
systemd-coredump:x:999:

fields:

group_name:enc_passwed:GID:members

## Process UID and Set UID

- Every process has associated UID and GID

- These UID dictates what the process can do on a given resource.

### Four user ID's associated with process:
    1. real userid and groupid: These are the group id used by the programs launched by a given user. Login shell sets this to the UID of user upon login.
    2. effective userid: This is UID under which the process is currently running. All permissions are checked again this.
    3. Saved user-id: This is the user-id which is usually realid of process before exec is called
    4. Save group-id

    - set user and group id: A program when run, runs under the priviledges of current user. However, if needed it can be run as privilege of other user who owns it. Example: su. This is done by setting the setuser/group bit. Commands:

chown root program
chmod u+s program

Now when the program runs as a different user, it will still run as if root is running it.

# Time

## systemcalls:
    - gettimeofday()
    - time()- redundant
    - stime()

## Notes:
- Two kinds of times:
    - Process Time: Amount of CPU TIME used by the processor
    - Real Time: Calendar time (local time), EPOCH, or time stamps used by databases etc

### Real Time:
- EPOCH: Number of seconds elapsed since 1 Jan 1970 (Birth of Linux). gettimeofday() and time() syscall returns this as a time_t type value.
- Time conversion functions:

Figure 10-1 here

- Time zones: /usr/share/zoneinfo file contains the information about timezones in a particular country.

- Locales: Every country has different conventions for representing data. date, currency is represented in different way in different countries: dd/mm/yy in US. For currency 100,99 in europe where , separate the decimal point.
    - Internalization or I18N of programs is a complex topic. Glibc provides libraries in /usr/lib/locale containing the directories for each locale which can be used by various programs for localization.

### Process time:
    1. User CPU Time (virtual time): Amount of time spent by the process in the userspace.
    2. System Time: Amount of time spent by a process in Kernel Space- that is kernel executing tasks on be-half of process such as servicing pagefaults, executing systemcalls (memory allocation etc)

- time command in unix can be used to get a processes user and system time. Real time here is sum of these two.

- Refer to Linux Userspace Kernel space article for more details.



# Proc filesystem
- /proc is a virtual file system which provides access to kernel information. It is window to the kernel operations.

- It is virtual file system because it does not reside on disk but rather kernel creates them on the fly.

- For each process, kernel provides a directory named /proc/PID.


## Directories / Files under /proc

1. /proc/PID
    - status -> shows process memory, cpu etc info.
    - cwd
    - fd (dir)
        - proc/PID/fd: Contains symbolic link for the fd used by process. Each process has 0, 1 and 2 fd 

            ```
            root@vinlok-ThinkPad-T400:/proc/1734/fd# ps -ax | grep bash
            1734 pts/0    Ss     0:00 bash
            3040 pts/0    S      0:00 -bash
            8040 pts/2    Ss     0:00 -bash
            8066 pts/2    S      0:07 -bash
            174261 pts/2    R+     0:00 grep --color=auto bash
            root@vinlok-ThinkPad-T400:/proc/1734/fd# ls -l /proc/1734/fd/
            total 0
            lrwx------ 1 vinlok vinlok 64 Oct 17 08:51 0 -> /dev/pts/0
            lrwx------ 1 vinlok vinlok 64 Oct 17 08:51 1 -> /dev/pts/0
            lrwx------ 1 vinlok vinlok 64 Oct 17 08:51 2 -> /dev/pts/0
            lrwx------ 1 vinlok vinlok 64 Oct 17 08:51 255 -> /dev/pts/0
            ```


    -  dir /proc/PID/task: Contains details for each thread groups as subdirectory under /proc/PID/task/TID. The files under the TID directory are exactly same those found under /proc/PID. 
    - cmdline: Command line args to the process
    - environment: Env variables to the process
    - Limit: resource limits.

2. dir /proc/net: Networking and socket. 

3. uptime: Seconds uptime and Time spent idle. 
```
root@vinlok-ThinkPad-T400:/proc/net# cat /proc/uptime
344015.42 364623.42
```

4. /proc/cpuinfo

5. /proc/meminfo

6. dir /proc/sys/kernel:
    - ostype
    - osrelease
    - hostname
    - domainname
    - pid_max
    - hs_last_pid used

7. dir /proc/sys/fs:
    - file-max

    