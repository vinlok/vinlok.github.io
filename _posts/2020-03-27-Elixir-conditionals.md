---
layout: post
title: "Elixir Conditional Statement"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Elixir case, if else statement.

<!--more-->

# case

```
  {response,binary} = File.read(filename) #This is a tuple
    case response do
      :ok -> :erlang.binary_to_term(binary)
      :error -> "File does not exist"

    end

```

# cond
- Conditions are similar to case statement. Syntax is as below:
```
cond do
      user = user_id && Repo.get(User, user_id) -> # if user_id is true && Repo.get returns user assign the value to user and enter this block
        assign(conn,:user,user) #assign is comming from plug.conn

      true -> # if user_id is not true then enter this block
        assign(conn,:user, nil)
    end

```

- In cond statement, the first statement which is matching as true gets executed.
- The true statement is catchall block here.
