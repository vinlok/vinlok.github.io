---
layout: post
title: "Elixir Atoms"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---


Atoms technically are just another datatype in elixir.

Atoms:
- Starts with :
- can contain _ and @ symbols. Examples: vinayak_lokhande, vinayak@lokhande
- can be string: 'vinayak lokhande'
- keep it simple by using all lowercase.
- have a value same as that of the text. Example:
- They are something similar to string.

```
iex(6)> :vinayak
:vinayak
```

- Elixir atoms can be used to do pattern matching as below:

```
defmodule Drop do
  @moduledoc """
  Documentation for Drop.
  This module contains funtions using patten matching using the atoms for functions
  """

  @doc """
  fall_velocity function for earth, moon and mars

  ## Examples

      iex> Drop.hello()
      :world

  """

  import :math
  
    def fall_velocity(:earth, distance) when distance > 0 do
        :math.sqrt(2*9.8*distance)
    end 

    def fall_velocity(:moon, distance) when distance > 0  do
        :math.sqrt(2*1.6*distance)
    end 

    def fall_velocity(:mars, distance) when distance > 0 do
        :math.sqrt(2*3.6*distance)
    end 

  @doc """
  new_velocity function for earth, moon and mars

  ## Examples

      iex> Drop.hello()
      :world

  """

    def new_velocity(distance) do
        :math.sqrt(2*2)

    end
end

```

## Atomic Booleans

- true , false are actually :true and :false
- you can do something like this:
```
iex(15)> 3 < 2
false
iex(16)> 3 > 2
true
iex(17)> true == :true
true
iex(18)> true == vin
** (CompileError) iex:18: undefined function vin/0
    (stdlib) lists.erl:1354: :lists.mapfoldl/3
    (stdlib) lists.erl:1355: :lists.mapfoldl/3
iex(18)> true == :vin
false
iex(19)> false == :false
true
iex(20)> 3 > 2 and 3 < 4
true
iex(21)> 3 > 2 or 3 < 4
```
- and , or, == are logical operators in elixir and take two arguments
- not is another logical operator which only takes one argument

## Guards

- You can add when condition to function as show above which will act as guards

## Tuples

- Elixir can combine multiple datatypes into single composite datatypes making it easier to pass messages accross components
- Tuples are declared using {}
- they optinally start with atom to declare what this tuple consists of.
### Tuples as pass through to private functions.
- Tuples can be used to access the private functions defined in an module:

```
defmodule Drop do
  @moduledoc """
  Documentation for Drop.
  """

  @doc """
  Hello world.
  """
    def fall_velocity({planemo,distance}) do
        fall_velocity(planemo,distance)
    end

    defp fall_velocity(:earth, distance) do
        :math.sqrt(2*9.8*distance)
    end 

    defp fall_velocity(:moon, distance) do
        :math.sqrt(2*1.6*distance)
    end 

    defp fall_velocity(:mars, distance) do
        :math.sqrt(2*3.6*distance)
    end 
end

```