---
layout: post
title: "Ulimit: 'Too many open files' explained"
date: 2014-01-25
categories: ['Linux']
excerpt_separator: <!--more-->

---

Every system administrator in his lifetime encounters this error: "Too Many open files". To summarize, this error tells that a given process has hit the limit on max number of opened files by it.

With the help of python code, we will see how to simulate this error and also see various config files associated with setting this parameter.
<!--more-->

### Ulimit:

- ulimit command can be used to set limit for number of files, processes etc.. at per user and per process level.
- Sample out from ulimit -a:

<pre>

[root@ip-10-0-0-46 ~]# ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 3891
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1600
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 10240
cpu time               (seconds, -t) unlimited
max user processes              (-u) 3891
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited

</pre>>


- You can change the ulimit for you current session as below:

	ulimit -n 1024

	Note that this will change the open files limit only for the current session.

- The max you can set this limit is configured in /etc/security/limit.conf and /etc/security/limits.d/<various-files>.

- Below excerpt from an Red Hat KB explains the order of precedence for these files:

	After reading /etc/security/limits.conf, individual files from the /etc/security/limits.d/ directory are read. The files are parsed one after another in the order of "C" locale. So the order will be special characters, numbers in ascending order, uppercase letters and lowercase letters in alphabetical order. If two files have same entry, then the entry read last will be taken in effect. Only files with *.conf extension will be read from this directory.

- Any changes in these files needs a reboot for them to take into effect.


## Understanding ulimit with help of example:

- Lets use the below python code to simulate opening of files:

<pre>

import time

fpd=[]
#The below block will open 2000 files AND NOT close them
for i in range(1,2000):
  fname = str(i)
  try:
  	fpd.append(open(fname, "wb"))
  	print "No of files opened:", i
  except Exception as error:
	print error

time.sleep(100)

</pre>>

### Scenario 1:
- /etc/security/limits.conf number of files limit set to: * soft nofile 1800
- There is no file with name *-nofile.conf created in /etc/security/limit.d/
- Ulimit will be set to 1800, which can be checked with ulimit -n command:

<pre>
[root@ip-10-0-0-46 ~]# ulimit -n
1800
</pre>>

- Lets run the above python code and you will see that it will error at 1800 limit:


<pre>
No of files opened: 1783
No of files opened: 1784
No of files opened: 1785
No of files opened: 1786
No of files opened: 1787
No of files opened: 1788
No of files opened: 1789
No of files opened: 1790
No of files opened: 1791
No of files opened: 1792
No of files opened: 1793
No of files opened: 1794
No of files opened: 1795
No of files opened: 1796
No of files opened: 1797
[Errno 24] Too many open files: '1798'
[Errno 24] Too many open files: '1799'
[Errno 24] Too many open files: '1800'
[Errno 24] Too many open files: '1801'
[Errno 24] Too many open files: '1802'
[Errno 24] Too many open files: '1803'
[Errno 24] Too many open files: '1804'
[Errno 24] Too many open files: '1805'
[Errno 24] Too many open files: '1806'
[Errno 24] Too many open files: '1807'
.
.
.
</pre>>


### Scenario 2:
- /etc/security/limits.conf number of files limit set to: * soft nofile 1600
- There is a file with name 90-nofile.conf created in /etc/security/limit.d/ with:  *          soft    nofile    1600
- Ulimit will be set to 1800, which can be checked with ulimit -n command:
<pre>
[root@ip-10-0-0-46 ~]# ulimit -n
1600
</pre>>
- Running the above python code will show that it will error at 1600

# Notes

1. Ulimit is shell builtin function. 
# Syscalls used to setup ulimit

- getrlimit()
- setrlimit()
- prlimit()



