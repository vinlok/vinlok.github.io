---
layout: post
title: "Python Cheatsheet"
date: 2016-12-25
---

# Doc Strings

- Doc strings are a way to document your python function, module etc. This doc can then be retrieved by using "dir" on the function, module etc.
- They are declared with """ Your description here """ and can span over multiple lines.
- Follow the best practices such as first line should be small and begin with capital letter and end with .
- If more lines are needed lines, the second line should be blank.

# Intermezzo coding style

- Use 4-space indentation, and no tabs.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4). 


# Input:

- Input in python can be done using: a = raw_input()

# List:

- List are declared 

List items need not be of same type:

a = ['spam', 'eggs', 100, 1234]

Indices starts at 0.

thus, a[0] means 'spam'

List as mutable. You can change a specific indices of list

len() also applies to list


Build in function insert:

a.insert(0,"bin")

['bin', 'spam', 'eggs', 100, 1234] 


Checking for given value in list

if bin in a:
     print "found"
