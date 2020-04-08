---
layout: post
title: "Elixir Functions basic"
date: 2020-04-1
excerpt_separator: <!--more-->
categories: ['Elixir']
---

This post talk about basics of elixir functions

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

