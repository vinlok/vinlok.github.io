---
layout: post
title: "Elixir Conditional Statement"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Elixir case, if else statement.

<!--more-->

#case

```
  {response,binary} = File.read(filename) #This is a tuple
    case response do
      :ok -> :erlang.binary_to_term(binary)
      :error -> "File does not exist"

    end

```