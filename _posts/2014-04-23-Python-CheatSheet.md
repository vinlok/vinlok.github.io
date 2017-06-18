---
layout: post
title: "Python Cheatsheet"
date: 2017-3-25
excerpt_separator: <!--more-->
---

Python is a programming language that lets you work more quickly and integrate your systems more effectively - From python.org.
Wherever you there is a need of fast prototyping, Python is the most apt candidate. While is arguably not a full object oriented language, however, it philosophy of "batties included" makes it one of the most popular language.

In this blog, we will go through the basics of Python and some of the best practices that I have learned.

<!--more-->

### Doc Strings

- Doc strings are a way to document your python function, module etc. This doc can then be retrieved by using "dir" on the function, module etc.
- They are declared with """ Your description here """ and can span over multiple lines.
- Follow the best practices such as first line should be small and begin with capital letter and end with .
- If more lines are needed lines, the second line should be blank.

### Intermezzo coding style
- Use 4-space indentation, and no tabs.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4). 


### Input:
- Input in python can be done using: a = raw_input()

### List:
> - List are declared using square brackets. 
> - Items in a list need not be of same type:

> a = ['spam', 'eggs', 100, 1234]

> - Indices starts at 0. Thus, a[0] means 'spam'

> - List are mutable. You can change a specific indices of list

### Useful functions
> - To get length : len()
> - To insert an element : insert()

>> a.insert(0,"bin")

>>['bin', 'spam', 'eggs', 100, 1234] 

> - Checking for given value in list
>if bin in a:
     print "found"

### Loops:
>#### While:
>>syntax :

>>while b < 100:
     print b

>#### For:
>>words = ['cat', 'window', 'defenestrate']

>>for w in words: 

>>... print w, len(w) 


>### range() function:

>>- Range function is quivalent of sequence function of list:

>>range(10)

>>range(5,10)

>- It can be used to iterate over in for loop. Example:

>>for i in range(10):


>- You can iterate over an list using len and range combination:

>>a = ['Mary', 'had', 'a', 'little', 'lamb']
>> for i in range(len(a)):
>>...     print i, a[i]

### Command Line Arguments

> Module: import sys

> Starts with  0. 0 is the name of the script invoking it.

> sys.argv[1]

> len(sys.argv)

# File I/O

> file object = open(file_name [, access_mode][, buffering])

> *Below are the supported access modes:*

>> r	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

>> rb	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

>> r+	Opens a file for both reading and writing. The file pointer will be at the beginning of the file.

>> rb+	Opens a file for both reading and writing in binary format. The file pointer will be at the beginning of the file.

>> w	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

>> wb	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

>> w+	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

>> wb+	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

>> a	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

>> ab	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

>> a+	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

>> ab+	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.


> **Examples**:
>> Opening a file:
>> \#!/usr/bin/python 

>> \# Open a file 

>> fo = open("foo.txt", "wb") 

>> fo.write( "Python is a great language.\nYeah its great!!\n"); 

>> \# Close opend file 

>> fo.close()

>> Read file into array:

>>\#!/usr/bin/python

>> import os

>> import pdb

>> with open('/tmp/serverlist') as f:

>>    server_names = f.read().splitlines();

>>    for i in range(len(server_names)):

>>    print server_names[i]

### Function:

> - Defining a function:

<pre> def fib(n):  # This defines the function
"""Write what you want to say about the function. This will be referred when some one has to browse through the function code"""
for i in range(n):
print i </pre>

> - Arguments passed to functions in Python are call by value. i.e., when the function is called from the program, the variables are actually copied to the function as new symbol table.


> - Values Returned by functions:
>> By default all function would return "None" value.
>> You can have a function return a specific value:

<pre> def add(a, b):
...     c=a+b
...     return c
...
>>> add(4,5) </pre>

> - A method is a function that ‘belongs’ to an object and is named obj.methodname, where objis some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type. Different types define different methods. Methods of different types may have the same name without causing ambiguity. 
