---
layout: post
title: "Graphs - Basics"
date: 2016-12-25
categories: ['Algorithm']
excerpt_separator: <!--more-->
---

Type of graphs, different ways to represent graphs using data structures
<!--more-->

# Types
1. Undirected graphs: Connection between the nodes is called as arcs. Arcs are represented as: arc(1,2) that is connection between 1,2 which is same as arch (2,1) as there is no direction.
2. Directed graphs: Connection between the nodes is called as edges
    1. DAG: Directed Acyclic graph: edge is represented as : edge(1,2)
3. Weighed graphs: These are directed graphs with values associated with the edges called as weight. The weight could represent distance, priority etc.
4. Trees: Trees are special type of graphs with zero cycles.
    1. in-tree: when the edges point towards the root
    2. out-tree: when the edges points outwards.

# Representing graphs
1. Adjacency Matrix
    - For weighted graphs: A[i][j] represents cost of moving from i to j.
    - For unweighted graphs: A[i][j] represents 0 of no path exists or 1 if exists
2. Adjacency List
    - [a:[(b,2),(c,1)]]
3. Edge List

# The Depth First Traversals of this Tree will be:
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)