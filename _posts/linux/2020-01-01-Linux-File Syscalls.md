---
layout: post
title: "Linux File Syscalls"
date: 2017-01-01
categories: ['Linux']
excerpt_separator: <!--more-->
---

 A System Call is controlled entry point into kernel allowing processes to request kernel to perform some actions on process behalf. Kernel makes range of services (or types of syscalls) available to processes via system calls using system calls API. Examples:

- Process Examples: Fork(), exec(), execv()
- File I/O
- Network Sockets
- Signals
- IPC
- Terminals
- Threads
- I/O Devices

# Steps involved in making a system call

Diagram here < System call>


# Library Functions

- These are the wrapper functions which the C programs call for performing specific actions.
- Not all Lib Functions do system_calls(). Example, string manipulation functions does not do system_calls. Where as other like fopen(), fwrite() are directly layered on top of open() and write() system calls.

- GLIBC has all the standard library functions we use. LDD can be used to find version of LIBC in use.

- Program can be compiled:
    - statically linked: Copies the actual function code into .text sections
    - Dynamically linked: name of library or Reference is added to code. These are in ELF format

    - ELF format looks as below:

        ELF diagram here


- Compilation steps:
    hello.c  ---> hello.i ---> hello.s(assembly) ----> hello.o(relocatable) ----> hello.out(executable program in ELF format)


- Errors from system calls are handled by the library functions. If the system call returns an error, the ERRORNO variable is set. using perror() and stderror() function these value can be retrieved and error can be printed.

Usually the function would return -1 and then we can use ERRORNO to retrieve the actual error.

```

#include <stdio.h>

main() {
   FILE *fp;
   int c;

   fp = fopen("/tmp/testi.txt", "r");
   printf("%d",(int)fp);
   if (fp == NULL){
	perror("open");
   }

}

```


# File I/O system calls

## basic I/O (Buffered at Kernel space level):

1. open(filename,flags,mode)
    - flags represent the mode of file to be open: 
    O_RDONLY
    O_WRONLY _> 
    O_CREAT -> If the name does not exist, create the file. If present do noting unless O_EXCL isused
    O_EXCL
    O_SYNC --> Do not buffer at kernel level
    O_NOBLOCK -->  Do not wait if no data is avail (example disk is waiting to read)

    open("somefile",O_CREAT|O_WRONLY|O_TRUNCATE)
    means create an new file in wronly mode and truncate it to size 0.
    Thisis equivalent to creat() system call.

    - mode: Permission to be placed on the file: rwxr-wr--

    - On success returns no-negative integer which is the smallest file descriptor avialble for the given process: usually it is 0 to 1024 but can be set.

    - On error returns -1 and set errorno variable. error can be retrieved using perror()


2. num_of_bytes_read_into_buff=read(fd,buffer,count_of_bytes)
    -fd is the file descriptor to read from, buffer is the buffer to read into, count_of_bytes is the max bytes to read.
    - returns -1 on error and sets errorno. On success returns the number of bytes read
    - returns 0 if EOF has been reached.
    - Read is always in blocking mode. That is if the file is not available to read, this call will wait until it becomes available.
    - -1 with EINTR is for blocking read when interrupt signal is received
    - -1 with EAGAIN is for non-blocking read when there is no data to read.

## Readahead:

![](2021-10-21-17-55-02.png)

3. n_of_bytes_written=write(fd,buffer,count_of_bytes)

    - returns -1 of failure and sets ERRORNO.
    - Partial writes can happen and should be check by comparing n_of_bytes_written with count_of_bytes 
    
    Write() are not written to disk immediately. Kernel usually buffers them as shown below:

    ![](2021-10-21-17-27-22.png)

    ### Writeback
    - Kernel has flusher threads which flush the contents of dirty buffers to disk periodically.
    - fsync() also forces kernel buffer to be flushed.

4. close(fd)
    - Returns -1 on error.

5. lseek(fd,offset,whence)
    - offset: number of bytes to move to
    - whence: base to move from: SEEK_CURR, SEEK_END etc

    ### Fileholes:
        - It is possible to write to arbitary location past the end of file. The space between the end of file and new location is called as hole. Core dump is example of sparsely populated files.

## Multiplexed I/O
- processes might need to read/write multiple file descriptors.
- This multiplexing is handled via poll() systemccall.
- poll() system call takes pollfd as struct which checks the file descriptors for events such as POLLIN (read) POLLOUT(write)

## User Buffered I/O
- Programs often issue many small I/O requests to files. Hence, user space buffering is employed rather asking kernel to buffer to avoid context switching.

- fread() and fwrite() systemcalls do not directly initiate disk access. Instead the data is copied between userspace buffer into kernel space buffer. Reasons:
    - Disks works in Logical blocks usually of 4K size.
    - Programs ofter work in chars and lines which might not be of same size.
    - Also, calling kernel to write/read to disk every time data is requested needs lots of context switches.



- Following diagram shows the process in detail:



- fwrite, fputs are stdio.h functions which provide buffered I/O. The size of the buffer can be changed and controlled using the setvbuffer() on the file descriptor.
    - setvbuff(fd,buff,mode,size)
        - where:
            - buff = buffer in memory
            - mode can be = _IONBF --> Do not buffer
                            _IOLBF --> Full buffer: Initiate write() system callwhen new line is encountered.
                            _IOBF- Block buffer,

- To force user user buffer, fflush() call can be used.

- kernel moves the buffer to disk whenenver it is full or if calls like fsync() are initiated. fsync() forces the kernels bufferes to be flused to disk.

- If a file is opened in O_SYNC mode, the every write() call results is flush call to disk.


- Here is the details syscall diagram for the same:

![](2021-10-18-13-40-47.png)


## Advanced I/O:

1. Scatter/Gather I/O or vectored I/O:
    - System call reads or writes from vector of buffers
    - readv() and writev()

2. mmap() or memory mapped I/O / files:
    - mmap take "len", "offset" and "fd" as argument. The data of size "len" is then mapped in to memory.
    - mmap() system call operates on pages. If then "len" is not multiples of page size then, the remaining mapped space is filled with zero's
    ![](2021-10-22-18-10-19.png)

    mmap to copy from one file to other:

    ```
    fd_in= open("input_file",readonly,perms)
    fd_out= open("input_file",readwrite, perms)
    
    src=mmap(sizeof_fdin,0,fd_in,PROTO_READ)
    dst=mmap(sizeof_fdin,0,fd_out,PROTO_READ|PROTO_WRITE)

    memcpy(src,dst)

    msync(dst)

    ```
3. mprotect() system call can be used to change the access mode of a given block of memory mapped by mmap() system call.

4. msync() call can be used for syncing back content of buffer to a mapped file.

5. readahed() system call provides mechanism to read n bytes of files into pagecache ahead of time.


# I/O scheduler

- The Logical Blocks Address (or logical blocks) map to CHS address.
- Disk seeks are 25 million times of one CPU cycle.
- To avoid disk head moving hap hazardily I/O schedulers perform two mechanisms:

1. Merging: if there is a request for block number 4 and then there is another request for block 5-8, these requests are merged together into 1 as 4-8 and then submitted.

2. Sorting: Requests to blocks 23, 9 , 1 and 10 are sorted as 1,9,10,23. If a new request comes for block 5 it is inserted at correct place and sent. This way head moves in linear fashion.

## *Read latency* 
- When data is not present in page cache, it has to be read from the disk and then cache updated and then data given back to process. This blocks the process till the time data is fetched from disk which is lengthy operation and called as disk latency.

## *writes-starving-reads*

- Read operations are sequential. If data is read from file in chuncks, before reading the next chunk, the previous chunk needs to be done. Thus, we need to do Disk I/O 
- Writes on other hands do not depend on disk I/O as the write are written at some later stage and these requests are streamed. Thus writes can consume all of kernel time starving reads.

- As the requests to blocks are sorted by block numbers and served, it is possible that a given block is starved and served after long time. To avoid this, there are different schedulers:

1. Linus elevator scheduler: 
 - Sort blocks by number in sorted_queue = 1(r),10(r),11(w),15(r),30(w)
 - service one at the head of sorted_queue 30(w)
 - If any item is older than exptime of sorted_queue service it first.

    Too simple heuristic and was decom in 2.4

2. Deadline I/O scheduler: 
- Maintains 
    - sorted_queue by block number = 1(r),10(r),11(w),15(r),30(w)
    - read_fifo by submission times = 1(r),15(r),10(r)
    - write_fifo by sub times = 30(w),11(w)
- Serves from head of sorte_queue
- If oldest item expires, it serves from head of respective queue. Example if 1 has expired, head from read_fifo queue which is 10 will be served.

3. Anticipatory I/O scheduler
- Deadline scheduler has lot of switching between read and write FIFO queue.
- Generally reads are more than writes. 
- Serves requests as above algo, however, before moving to next requests, it sits ideal in anticipation that request near to a given block will be submitted

4. CFQ:
- Each process gets its own queue and each queue is assigned a time slice.
- RR mechanism between queues are employed.
- If there are no requests in a given process queue, CFQ sits in that queue for 10 ms in anticipation that something will come. If not, move to next.

5. Noop: 
- Does only merging no sorting
- Used generally by SSD.

Optimizg for I/O performance:
- Peform block size aligned I/O
- User user space buffering (printf, fwrite stdio buffering)
- Schedule I/O in user space:
    - Sort by file path. If there are multiple requests made to files, generally files in the same directory will be closer. Hence, make the requests by sorting by file path

    - Sort by inode. inode of file can be figured out by inode.
    - soft by physical block:
        ```
        - get the blocks of file using stat()
        - get the physical blocks using ioctl()
        ```

    


# 

- 
- 
