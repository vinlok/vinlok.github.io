---
layout: post
title: "Linux Processes"
date: 2017-01-01
categories: ['Linux']
excerpt_separator: <!--more-->
---


# Processes

- A process is instance of running program. 

- A program is a file containing information that describes how to construct a process at run time. It includes:
    - Binary Format Identification: a.out (Assembler Output), ELF
    - Machine-langauge instructions: The actual code of the program
    - Program entry-point address: Location of instruction to start execution
    - data: Initialized and uninitialized variables
    - Shared-Lib and dynamic linking info

<ELF digram here>

- Kernel stores list of running process in circular linker list and each element of LL is of type task_struct which is the process descriptor. This is usually 1.7 KB in size. It defines:
    - Open files(PPFDT)
    - Memory mapping(page table)
    - process state
    - pending signals
    - PID: PID of process is unique positive integer which can be accessed using getpid(). Once max limit has reached, kernel starts at 300 as less than 300 is reserved for system processes and daemons.
    - PPID: Each PID has a PPID which can be found using getppid()
    - ownership (user and group owner): real-userid, effective-uid, 
    - process group ID

- *Process Group*:
    - Each process is part of process group: child belong to same process groups as the parents. When shell starts a pipeline ls | wc -l here, ls and wc belongs to same process groups
    - Process groups makes it easy to send signal to group of interconnected processes.
    - process group is very closely related to job.
    - each process group is identified by pgid(process group id) and has a group leader and the pgid = pid of group leader.
    - When a user with UID 500 logs in, the bash is made as the leader of process group with pgid 500 and a new session is created with session id 500 
    - now when more process as launched, they all start with new process groups belonging to session id 500
    - When the users session finishes or user exits from session, all foreground jobs/process groups are sent SIGQUIT.
    - When network interupt is detected for shell, SIGHUP is sent all foreground process groups of a given session ID.
    - Ctrl+c send SIGINT to all foregroud process groups

    ![](2021-10-23-16-23-32.png)


### Daemon process:
    - Started generally as root or as special user
    - It must be started as child of init and not connected to any terminal.
    

# Memory Layout of a process

Consider the following C code:

```
#include <stdio.h>

int global_initialized = 21;

int global_uninitialized;

int function1(){

    int function1_local_var;
    int *pointer = malloc(sizeof(int));
    free(pointer)

}

int main(int argc, char *argv[]){
    int main_local_var;

    func();
    return 0;
}

```

The above code is compiled into ELF format described above and the memory map looks as below:

![](2021-10-19-15-57-48.png)


- The userstack grows and shrinks and functions are called an returned.
- The kerner-stack is per-process memory region maintained by kernel. This is used during the syscal execution. When library function executes trap, the kernel copies the registers(rdi...) to the kernel stack region of each process. 

## Heap

- Heap is present right after the uninitialized data segment in process memory map. 
- Heap is generally allocated using malloc()
- Malloc() function allocates size bytes from heap and returns pointer to the start of newly allocated block of memory. This block consists of pages. malloc return pointer of type void * which can be assigned to pointer of any c type.
- Free() function deallocates the memory block (or set of pages). It does not lower the program break (brk()) instead adds these block to list of available blocks.
- Next time when malloc requests for memory, it is given from these blocks if sufficient space is present.

# Virtual Memory - Processes

- VMM maps virtual address space to physical address space
- VMM helps with efficient use of CPU and RAM(physical Memory) by making use of locality of reference:
    - Spatial Locality: Access memory near to recently accessed.
    - Temporal Locality: Access same memory which was accessed recently

- Memory used by program is split into fixed size units called *pages*. Corresponding RAM is divided into Page Frames of the same size usually of 4 KB. Only some pages of program need to be resident in the RAM page frames. Unused pages are swapped. If a page is referenced that is not in RAM page fault occurs. Kernel loads this from disk.

- Kernel maintains page table for each process in the kernel address space of the process. This is not accessible to the process but is used by kernel. Thus the processes virtual address space which consists of pages (of size 4k) are mapped to corresponding Page Frame in RAM via page table:

- Processes are isolated from each other and memory is not shared unless explicitly done using mmap().

- As this is virtual, memory can be moved.

## MMU
- MMU does the mapping or translation of virtual to physical. Part of CPU.
- MMU has TLB which holds:
    1. virtual to physical addres
    2. Permission bits
- Page is the unit of memory it can work on usally 4 kb.
- Page frame is the page sized memory block again usually 4 KB. Kernel uses pfn to refer to physical page fram.
- 
- PageFaults as execptions raised when:
    1. If process is accessing a non-mapped virtual address.
    2. Process is trying to access memory when they do not have permissions
    3. The page has been swapped out to disk.


- Diagram below show the per-process virtual memory layout.
    - Kernel Logical Addresses:
        - Use fixed memory mapping and just like virtual space are physically contiguous. Thus can be used for DMA.
        - These cannot be swapped out.
    - Kernel Virtual Adresses:
        - There are no virtual addresses. And it is usally the reserved space of top of RAM.
        - vmalloc() is used to allocate this.
        - Non-contiguos

    - User virtual Addresses:
        - 3 GB of space on 32 bit systems.
        - Uses MMU
        - Can be swapped out.
        - Each processes has got its own memory map or page table which is part of kernel stack of that process.

    - Lazy allocation:
        - Kernel does not allocate physical memory immediately.
        - It allocates virtual memory but does not allocate physical memory until the process actually touches it.

### Page Tables:
    - The TLB is limited in size. Thus, it cannot hold the memory mapping for all the processes.
    - Kernel stores these memory mappings into page tables using struct_mm which is linked to process using task_struct (Process descriptor)
    - 

### Swapping
- When you are low on memory, kernel moves the unused page frames to disk and update the TLB.
- When the process tries to access the page (which is mapped to frame), page fault occurs and does this:
    - Put process in sleep
    - copy frame from disk to RAM
    - fix the page table to point to correct 
    - wake the process back up.



![](2021-10-15-17-11-39.png)




# Process and files relation

- For each process, kernel maintains a **per process file descriptor table** which stores:
    - pointer open file table description

- Kernel also maintains a global system-wide open file descriptions table which stores:
    - open file description id (number)
    - offset location in file (usually lseek() or if previous write() or read() has done that)
    - file access mode; ro, w, append
    - pointer to i-node entry or (i-node number)

- Following diagram shows this:

![](2021-10-19-17-25-57.png)

- Here process A and B share the 83 global open file description. Hence, if process A changes the offset, process B will see the same.

- Fork() of a process will usually result in this scenario.


# I/O redirection

- Each process has a PPFDT which has three default descriptors:
 - 0 --> stdin
 - 1 --> stdout
 - 2 --> stderr

![](2021-10-20-10-13-30.png)

# Process Creation

## exec family of calls

    1. execl(*path, *arg, ...): Replaces current running process by the program pointed by path.
        - it is a variadic funtion which mean arguments can follow one by one terminated by NULL.
        - usually the pattern is:
        ```
        ret = execl("/bin/vi","vi","test.txt",NULL)

        ```
        - On success execl does not return because the current program is being replaces with the new one and execution jumps to the new.
        - On error -1 is set and perror() can be used to retrieve the error code.
        - Everything of the parent process except the following is changed:
            - pid, ppid, priority, user and group owner remains same.
        - ppfd is shared with new process. Thus it will have access to list of open files by the old process.
        - 

    2. execv(*path,array_containing_args)
        ```
        char *args[] = {"vi","test.txt",Null}
        execv("/bin/vi",args)
        ```

    

## fork()

- Fork() system call creates a new child process which is an almost exact copy of the parent.

- The parent and child will have same text. However, they will have their separate copies of .data, .bss, heap, stack and kernel_code sections.

- Thus each process can modify there own set of variables in stack and access the heap.

```
main(){
    pstack=2

    pid=fork()
    if pid==0:
        //In child
        pstack +=1
        // Now pstack will be 3
    else:
        // in parent
        pstack += 2
        // Now pstack will be 2 +4

    // both child and parent will come here
    print(pstack) here pstack will be 3 for child and 4 for parent 
}

```

- The child also receives duplicate copy of parent PPFD.

```
main(){
    fd=open()
    lseek(fd,100,cur)
    pid=fork()
    if pid==0:
        //In child
        lseek(fd,1000,cur)
        // now fd will be 1100
    else:
        // in parent
        wait()
        // Now pstack will be 2 +4

    // both child and parent will come here
    print(pstack) here pstack will be 3 for child and 4 for parent 
}
```

- fork is done as below:

```
int shared_var=1

pid = fork();

if pid == 0:
    // Then this is child
else:
    // this is parent
    // Do parenting, which is usually to wait() for child :)

//both process will return here and execute remaining program

```

- shell does fork and exec on new process.

- 

### *Copy on write - COW*

- When fork system call is executed, following steps occur:
    - New process with copy of parents .text, .data, .bss,heap and stack is created.
    - However, instead of copying the actual memory pages the pages as marked readonly and COW attribute is set in pagetable and TLB.
    - When the child tries writing to a given page, as it is readonly pagefault occurs indicating COW attribute.
    - Kernel then copies the page for the child, clears the COW attribute of old page and makes it writable.
    - The child would then continue using the new copy of page.

- As fork is usually followed by exec() which usually replaces the content of process memory map, COW saves the hassel of copying.


## exit(exit_status)

- no return value as there is no place to return.
- exit_status of 0 means success.
- On exit, the process open files are flushed.
- When process exits, SIGCHLD signal is sent to parent.

## zombie process
- When child dies before the parent, then the child is considered as zombie.
- This happens when the parent does not wait for child to finish or has not reaped the status of child using the wait() systemcall:

```

#include<stdio.h>


void main(){
int shared_var=1;
int pid = fork();


    printf("%d\n",getpid());

    if (pid == 0){
    // Then this is child
        printf("In child\n");
        printf("%d\n",getpid());
        }
    else{
        // this is parent
        // Do parenting, which is usually to wait() for child :)
        printf("In parent");
        printf("%d\n",getpid());
        sleep(10);
        }

//both process will return here and execute remaining program
}

```

- These are called as ghosts processes. Essentially if a parent forks a process and does not wait upon it, kernel keeps a skeleton on if just incase parent wants to see it later. 

- Incase the parent dies before waiting on zombie, init is made as its new parent and the it is waited upon by init.


# Atomicity and race conditions

Race condition: Result produced by two processes operating on a shared resources depends unexpectedly on the relative order of these process gaining access to CPU.

![](2021-10-15-11-07-33.png)

In this case O_WRONLY flags does not ensure if the file is already open by other process or not. Hence, it might lead to race condition.