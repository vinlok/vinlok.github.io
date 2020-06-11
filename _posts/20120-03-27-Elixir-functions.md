---
layout: post
title: "Elixir Functions"
date: 2020-04-1
excerpt_separator: <!--more-->
categories: ['Elixir']
---

This post talk about basics of elixir anonymous functions and more

<!--more-->

- Functions are building blocks for modules
- Each function can have one or more than one arguments it takes. Example:

```
defmodule Cards do

  def create_deck do
    ["Ace","Two","Three"] ## This is how value is returned by default. No need of return statement.
  end

  def shuffle(deck) do # Here deck is the variable you pass to it.

  end

end

```

- In above example, create_deck has no arguments. Hence it is represented as create_deck/0
- and shuffle takes one argument, hence it is represented as shuffle/1
- The number of variables passed to functions/methods is reffered to as Arity for the method. Its represented as /1
- ? are valid in names of functions. Generally, if a method name contains ?, it is going to return "True" or "false" boolean value.
- Default parameter are passed to functions using \\ :

```
def changeset(struct, params\\ %{})do
    struct
    |> cast(params, [:title])
    |> validate_required([:title])
  end
```
---
## Anonymous Functions

**Defining an anonymous function:**
- They are first class values. Mean you can assign them using variables.
```
falling_velocity = fn(distance) -> :math.sqrt(2 * 9.8 * distance) end
```
- This can be read as:
bind falling_velocity variable to function (thus the falling_velocity can be treated as function name) which takes "distance" as input variables "() are optional" and yields or returns sqrt of 2 times 9.8 times distance and then ends

**Calling an anonymous function**
falling_variable.(20)
```
iex(30)> falling_velocity = fn(distance) -> :math.sqrt(2 * 9.8 * distance) end
#Function<6.128620087/1 in :erl_eval.expr/5>

iex(31)> falling_velocity.(20)
19.79898987322333
```
- You need the period between the variable name and the argument when you call a function that is stored in a variable.
- You can use the *capture operator &*  for defining the anonymouns functions:
```
falling_velocity =&(:math.sqrt(2*9.8*&1))
```

