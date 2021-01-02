---
layout: post
title: "Elixir reuse code using import, alias and use"
date: 2020-05-31
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Elxir has three ways to reuse code:
alias
import
use

<!--more-->

### Import
- This is used to import all functions of a module to other module.
- You can reference all the functions of module

### Alias
use this to reference function from other module. Example:

```
defmodule Math do
 def add(a,b ) do
    a + b
 end
end 

defmodule TopicConroller do
alias Math

def somefunction() do
add(1,3)
end

end

```
- When you call add in TopicController, it looks for the function. As it is not present, it will go to all aliased Modules and search for it there.
- Thus, all alias is doing is to save you from typing Math.
- When you alias a module, you can refer to it with the part after . Example:
```
alias Discuss.Topic

Now you can call functions within Topic just using:

Topic.somefunction()
```

### use
- Details to be added soon..