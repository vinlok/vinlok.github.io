---
layout: post
title: "Elixir Data Structures: Tuples, Lists, and Maps"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Elixir data structure can be classified into three types: Tuples, Lists and Maps

<!--more-->
### Tuples
- Represented by 
```aidl
iex(33)> {:first_element,"second_element", "third_element"}
{:first_element, "second_element"}
```
- Index starts at 0
- Should be used for reading. Generally used to return error codes, or a fixed set of values.

### Lists

- Are ordered set of similiar or dis-similar data type values
```
iex(13)> [1,2,3,4,5]
[1, 2, 3, 4, 5]
iex(14)> [1,a,2,b,3]
** (CompileError) iex:14: undefined function b/0

iex(14)> [1,"a",2,"b",3]
[1, "a", 2, "b", 3]
```
- You can use single quotes in list, however, it is a convention to use single quotes in Elixir code.

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
- To get the first three elements of List using pattern matching:
```
[first, second, third | _tail ] = somelist_of_arbitary length
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
#### Enum
- Shuffle list: 
Enum.shuffle([1,2,3])
- Contains
Enum.member?(enumerable,element)

### Maps

- Maps are collection of Key value pairs. Python world it is dictionary. Ruby world it is called as hash
- represented by %{k1: v1, k2: v2}
- note that key end with : and there is no space. Values after : needs a space.
- other way to represent:

- Maps are not ordereded, hence, unlike list, accessing maps is not a linear operation.
#### Fetching values in map
- If the map key is described as atom:
```aidl
iex(45)> m1=%{hello: "world"}
%{hello: "world"}
iex(46)> m1[:hello]
"world"
iex(47)> m1.hello
"world"
```
then:
  - Values for keys can be accessed using map_name.key or map_name.atom.
  - or map_name[atom]
 
If not, then use function:
```aidl
iex(31)> a=%{"hello" => "world"}
%{"hello" => "world"}
iex(32)> Map.fetch(a,"hello")
{:ok, "world"}
``` 

#### Patten Matching in Maps
- Consider an example map: colors = %{primary: "red", secondary: "blue"}
- To access primary, you can do:
```
iex(6)> colors = %{primary: "red", secondary: "blue"}
%{primary: "red", secondary: "blue"}
iex(7)> %{primary: value} = colors
%{primary: "red", secondary: "blue"}
iex(8)> value
"red"
```
#### Updating a map
- Recap: data structure in Elixir are immutable. Elixir does not change a exiting DS, but copies it after making changes
- Two ways of updating or manipulating maps:
1. Using functions:
- https://hexdocs.pm/elixir/Map.html#content
- example:
```
iex(14)> a=%{"hello" => "world"}
%{"hello" => "world"}
iex(15)> Map.put(a,"hello", "vin")
%{"hello" => "vin"}
iex(16)> a=%{"hello" => "world"}
%{"hello" => "world"}
```
- note that the value of "a" remains unchanged. Map.put created a new map.

2. Using |
```aidl
iex(17)> a=%{"hello" => "world"}
%{"hello" => "world"}
iex(18)> %{a | "hello" => "vin"}
%{"hello" => "vin"}
```

### Keyword List
- List containing 2 element tuples of any length
- Represented as: [{a,b},{c,d}]
- Can contain duplicate key's (key difference from map):
```aidl
iex(40)> k=[{:key1,"value1"},{:key1,"value2"}]
[key1: "value1", key1: "value2"]
iex(41)> Keyword.get_values(k,:key1)
["value1", "value2"]
```
- Operations on Keyword list are linear. As the length of keyword list increses, the time needed to perform and operation also increase

### Struct
- Structs are just like maps with two special things you can do on it:
    1. You can assign default values
    2. There is compile time checking for data stored in structs.
- Struct enforce that the only property you can add to struct is the property you add to struct.
- Structs cannot hold and functions or methods in them. This is a key difference from the ruby, java etc languages.
- The syntax to access Struct is same as that of map:
```
%struct_name()
```
#### Updating structs
- updating structs works the same way as that of maps. You can use function or the pipe operator. Refer to updating maps section.