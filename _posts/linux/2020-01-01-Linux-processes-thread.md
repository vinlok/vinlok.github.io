---
layout: post
title: "Linux Processes - Threads"
date: 2017-01-01
categories: ['Linux']
excerpt_separator: <!--more-->
---

- If a process contains single thread, it is called single threaded else, multi threaded.

- Virtual memory is associated with process but not threads.
- Virtualized processor is available to threads and not to processes.

# Why Multithreading?   

- Style of programing or programming preference.
- parallelism
- Task delegation: Example: part of program which waits for use input can be delegated to a thread whereas other part can continue executing.
- Low context switching between threads as VMM is same.
- Processes are not expensive but threads are cheaper!

# Threading Models

Two types:
- Kernel level: Thread in kernel translates to user-space concept of thread
- User-level threading: This is N:1 threading. Threads are only implemented in userspace and kernel is not aware of it. Not good for modern hardware as we have multi cpu systems.

# Threading patterns

## Thread-per-connection
    - Unit of work gets its own thread. Example: webserver serving request, or connection gets its own thread.
    - Here the thread will run until the connection or request or unit of work is over.
    - Generally used in I/O. As I/O is blocking, the threads get blocked until it is available.
    - Apaches standard fork follows this.

## Event Driven Threading

    - For thread-per-connection approach, with thousands of connections we will need thousands of threads. This might be counter productive as generally if you have more threads that processors.
    - 


# Concurrency vs Parrellism

- Concurrency can happen on single CPU systems. Here multiple threads get executed concurrently.

- Parrellism: This is also called true parallelism needs multiple CPU. Here, two or more threads are actually run in parallel on multiple CPU's.

# Race conditions:
- Race conditions happen when two threads/processes are accessing the same shared resources and outcome is dependent on the scheduling of other.
- Example: Consider x++. This can be broken down into:
    1. Load value of x(5) in register 
    2. Increment the register value 5 by 1 = 6
    3. Store back the register value to = 6

    If two threads are working on this, then this might happen:



    Thus here, x++ becomes critical region code and needs to be handled.

- This can be solved using synchronization that is the critical region of the code must be done mutually exclusive.

## Mutexes

- Locks are used to enforce mutual exclusions hence know as mutexes.
- Steps:
    1. Locks is defined by programmer.
    2. It is acquired before entering a critical region.
    3. Lock can be held only by one thread at a time, thus, if in use, other thread has to wait.
    4. When done, release the lock and let other use it.


# Deadlock
- Deadlock is a condition when two threads are waiting for each other to finish.

- ABBA is an example of this:
    - Here Thread 1 gets its first mutex A and thread B gets its first mutex B
    - But when thread 1 tries to acquire its second mutex B and likewise thread B tries to acquire its mutex A, both have to wait!

# Pthreads : Linux threading implementation

Linux threads was the old way of doing pthreads. 

The new way is Native Posix Thread Library: It uses clone() system call and treats threads just as processes sharing some resources.

pthread API is user space and defined in pthread.h

```
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

void * start_thread (void *message)
{
        printf ("%s\n", (const char *) message);
        return message;
}

int main (void)
{
        pthread_t thing1, thing2;
        const char *message1 = "Thing 1";
        const char *message2 = "Thing 2";

        /* Create two threads, each with a different message. */
        pthread_create (&thing1, NULL, start_thread, (void *) message1);
        pthread_create (&thing2, NULL, start_thread, (void *) message2);

        /*
         * Wait for the threads to exit. If we didn't join here,
         * we'd risk terminating this main thread before the
         * other two threads finished.
         */
        pthread_join (thing1, NULL);
        pthread_join (thing2, NULL);

        return 0;
}
```
