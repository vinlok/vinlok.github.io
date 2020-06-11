---
layout: post
title: "Elixir Pattern Matching"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Pattern matching is the core of Elixir. It is Elixir's replacement for variable assignment. Using pattern matching, Elixir assigns values to variables.

<!--more-->

- Lets assume you have tuple : {First_element, Second_element}. Elixir will do pattern matching as below using which you can access the first and second element. This is similar to Python:

{f,s} = {First_element, Second_element}

- pattern matching is employed when you use "=" sign. Example:
```
normal_variable=["value1"]
```
Here as the left hand side of the = is "normal_variable", entire list is assigned to it.

- You can do something like this:
```
[value] = ["value1"]
```

- If not matching, it will thrown error:
```
iex(23)> [value] = ["value1","value2"]
** (MatchError) no match of right hand side value: ["value1", "value2"]
```

- Pattern matching using Case statement
```
    case File.read(filename) do
      {:ok,binary} -> :erlang.binary_to_term(binary)
      {:error,reason} -> "File does not exist, got #{reason}}"
    end
```
Here, the reponse of File.read is a tuple. Value at Index[0] of tuple is status(:ok or :error) and at Index[1] is payload/data.

in the case statements, elixir will match the left hand side whenever the response is :ok and execute the binary_to_term statement.
If the response is :error, then the reason will be stored in "reason" variable and passed on to right side.

