---
layout: post
title: "Elixir Lists"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Blog about list

<!--more-->

## Lists

- Are ordered set of similiar or dis-similar data type values
```
iex(13)> [1,2,3,4,5]
[1, 2, 3, 4, 5]
iex(14)> [1,a,2,b,3]
** (CompileError) iex:14: undefined function b/0

iex(14)> [1,"a",2,"b",3]
[1, "a", 2, "b", 3]
```

- List can contain sublist
```
iex(15)> sublist=[1,2,3]
[1, 2, 3]
iex(16)> mainlist=[1,2,sublist,4,5,6]
[1, 2, [1, 2, 3], 4, 5, 6]
```
- You can flatten a list using List.flatten/1 function as below:
```
iex(17)> List.flatten(mainlist)
[1, 2, 1, 2, 3, 4, 5, 6]
```

- To produce a single list from multiple list flattened by default, you can use the Enum.concat/2 function or the equivalent ++ operator.
```
iex(18)> a = [1,2,3,4]
[1, 2, 3, 4]
iex(19)> b=[5,6,7,8]
[5, 6, 7, 8]
iex(20)> a ++ b
[1, 2, 3, 4, 5, 6, 7, 8]
```
- Head and tail on lists: You can get the first element and the rest of the element of a list as below:
```
iex(21)> list=[1,2,3,4]
[1, 2, 3, 4]
iex(22)> [h1|t1]=list
[1, 2, 3, 4]
iex(23)> h1
1
iex(24)> t1
[2, 3, 4]
iex(25)> [h2|t2]=t1
[2, 3, 4]
iex(26)> h2
2
iex(27)> t2
[3, 4]
iex(28)> [h3|t3]=t2
[3, 4]
iex(29)> h3
3
iex(30)> t3
[4]
```

```
defmodule Overall do
  def product([]) do
    0
    IO.puts("in 1")
  end

  def product(list) do
    product(list, 1)
    IO.puts(inspect(list))
    IO.puts("in 2")
  end

  def product([], accumulated_product) do
    accumulated_product
    IO.puts("Product of elements of list is #{accumulated_product}")
  end

  def product([head | tail], accumulated_product) do
    product(tail, head * accumulated_product)
    IO.puts("in 4")
  end
end
```
