---
layout: post
title: "Elixir Modules"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---


## Modules:
- modules in elixir are formal places to put your code to share, code, encapsulate your code effectivetly
- Modules in elixir are collection of methods. There are no instance variables.
- Ideally, each module should go in its own directory with extension .ex. Format: name_of_module.ex, where name_of_module is the lowercase version of the module name you specify inside of the module file
- mix tool takes care of creating the .ex file as below:


Spliting code into multiple modules:
1. We started with Drop module, lets says we want to split this into 3 modules: 
    Drop: To calculate the velocity
    Convert: To covernt mps to mph and kph
    Combined: To call both the functions

2. To split, in the lib directory, we will create three files with modules for each:
    drop.ex
    convert.ex
    combined.ex
3. Now recompile and in the iex shell you can call the split modules as below:

```
Combined.height_to_mph(20)
```



### Importing functions explicitly:
- You can import function explicitlyin modules using:
```
    import Drop
    import Convert
```
- if you import the functions in the module, not in the function, then the scope of the imported modules is for all the functions
- importing an erlang module is done by prefixing it with ":" as below
```
import :math
or

import :math, only:[sqrt:1] #import only sqrt function with airity of 1 from the math module
```

### Module Attributes:
- Defined using @ 
- There are two predefined attributes @moduledoc @doc
- You can also define custom module attributes which are constant using @something
