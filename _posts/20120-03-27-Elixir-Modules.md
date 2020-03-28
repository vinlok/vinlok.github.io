---
layout: post
title: "Elixir Modules"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---


## Modules:
- modules in elixir are formal places to put your code to share, code, encapsulate your code effectivetly
- Ideally, each module should go in its own directory with extension .ex. Format: name_of_module.ex, where name_of_module is the lowercase version of the module name you specify inside of the module file
- mix tool takes care of creating the .ex file as below:

```
mix new ch02/ex1-drop --app drop
* creating README.md
* creating .formatter.exs
* creating .gitignore
warning: redefining module FirstApp.MixProject (current version defined in memory)
  /Users/vinlok/github/lokhanv1/learnings/first_app/mix.exs:1

Error while loading project :umbrella_check at /Users/vinlok/github/lokhanv1/learnings/first_app
* creating mix.exs
* creating config
* creating config/config.exs
* creating lib
* creating lib/drop.ex
* creating test
* creating test/test_helper.exs
* creating test/drop_test.exs

Your Mix project was created successfully.
You can use "mix" to compile it, test it, and more:

    cd ch02/ex1-drop
    mix test

Run "mix help" for more commands.
```

- In the above example, mix has created a directory ch02/ex1-drop, added a lib directory to it, and then finally added drop.ex to it:
```
├── ch02
│   └── ex1-drop
│       ├── README.md
│       ├── config
│       │   └── config.exs
│       ├── lib
│       │   └── drop.ex
│       ├── mix.exs
│       └── test
│           ├── drop_test.exs
│           └── test_helper.exs
```
- drop.ex would be poplulated with this:
```
defmodule Drop do
  @moduledoc """
  Documentation for Drop.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Drop.hello()
      :world

  """
  def hello do
    :world
  end
end
```

- now you can define functions in the module as below:

```
defmodule Drop do
  @moduledoc """
  Documentation for Drop.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Drop.hello()
      :world

  """

  def fall_velocity(distance) do
    :math.sqrt(2 * 9.8 * distance)
  done

  def mps_to_mph(meters) do
    2.23693629 * mps
  end

  def mps_to_kph(meters) do
    3.6 * mps
  end
end
```

**Compiling Code**

Steps:
1. You need to be in project directory created by mix command
2. Run iex -S mix :
    -S takes the mix.exs as argument. This script is generated when you created the project using the mix new command
3. This will fire up the iex shell and compile the mix.exs script
4. If you have made changes to the .ex file, you can recompile using the "recompile command"

**Running the compiled code**

Steps:
1. Once you have compiled the code using the iex -S mix command, you will be in the shell as below:
```
iex -S mix
Erlang/OTP 21 [erts-10.1.1] [source] [64-bit] [smp:8:8] [ds:8:8:10] [async-threads:1] [hipe] [dtrace]

Compiling 1 file (.ex)

call the function as:

module.function_name(argument_value)
Drop.fall_velocity(20)
```

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
