---
layout: post
title: "Python DS Time Complexities"
date: 2017-3-25
categories: ['Python']
excerpt_separator: <!--more-->
---



# Arrays
## Key points:
    1. Fast retrieval. O(1) to retrieve element at given index
    2. Fast Append: O(1) if array has space.
    3. Costly inserts and delete: O(n) if insert at 0 as you need to scoot each element

## Time Complexity:
```
Insert, delete: O(n)
Append: O(1)
retrieve single element: O(1)
element in array: O(n)
```

# Dynamic arrays:
## Key points:
    1. Arrays with automatic resizing.
    2. Appends worst case O(n). Amortized: O(1)
    3. Size of arrays and capacity are different. end_index is used to keep track of capacity.
    
## Time Complexity:
```
Insert, delete: O(n)
Append: O(1) amortized and O(n) worst case
retrieve single element: O(1)
element in array: O(n)
```
# Linked List:
## Key Points:
    1. No native Python implementation

## Time Complexity:
```
Insert, delete: O(n) 
Append or pre-pend: O(1)
retrieve single element: O(n)
element in array: O(n)
```


# Queue:
## Key Points:
1. Used in BFS
2. FIFO

## Time Complexity:

```
enqueue(push) and deque(pop): O(1) 
```

# Stack:
## Key Points:
1. Used in DFS
2. LIFO


# BST:

## Time complexity:
1. Balanced:
insert, search/lookup,delete: O log(n)

2. Un-balanced:
insert, search/lookup,delete: O (n)

# Dictionaries:
## Key Points:
1. Fast lookups of O(1)
2. If all the keys cause hash collision, then the lookups would take O(n) as it is similar to traversing the linked list.


## Time Complexity:



# Strings:
1. Strings are immutable. To change a string:
    1. convert to list
    2. make changes
    3. convert back to list.

2. 


# References:

- https://www.interviewcake.com/concept/python/hash-map?#when-lookups-cost-o-n