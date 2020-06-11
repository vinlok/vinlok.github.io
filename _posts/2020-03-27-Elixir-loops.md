---
layout: post
title: "Elixir Loops"
date: 2020-04-08
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Post about various ways to loop over in Elixir

# For loops

- List comprihension can be done as below
``` 
for suit <- suits do ## Iterate over every element in suits list/map.
    suit 
end
```
- This inherently returns a map.


