---
layout: post
title: "Elixir Functional vs OOP languages"
date: 2020-03-31
excerpt_separator: <!--more-->
categories: ['Elixir']
---

This post talk about key differences between OOP vs Functional languages.

<!--more-->

** Objects vs Functions
- OOP works on the concepts of classes and object. Classes are collections of instances and methods. You have classes and methods associated with it. You instantiate a class with objects and then access the methods and variables local to the object.

- Functional programing works on modules. It is collections of methods or functions. There are no instance variables. There is no concept of instantiate a module. And example flow is something like this:

1. Module will have a function which will produce a result/data.
2. The result/data is fetched to other function which can perform come action on it.

- In elixir, we never modify the original variable when it is passed to a function. Example:
```
a=[1,2,3]
Enum.shuffle(a)
```
Here a remains same. In the background, elixir will copy the var content in mem, and pass to Enum and shuffled contect will be returned. "a" variable remains same throughout.
