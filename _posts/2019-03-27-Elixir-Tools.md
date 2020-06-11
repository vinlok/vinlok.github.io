---
layout: post
title: "Elixir Tools"
date: 2018-05-13
excerpt_separator: <!--more-->
categories: ['Elixir']
---

This blog details various Elixir tools

<!--more-->

### Mix
Mix tool is installed default during the elixir installation on Mac using Brew. Mix can be used to:

1.  Create a new project
    ```
    mix new <projet name>

    mix new cards
    or
    mix new cards --app cards #to specify the name of module if it is differen than project name.
    ```
    This will create template files as below:
```
.
├── README.md
├── config
│   └── config.exs
├── lib
│   └── cards.ex --> This is where the code lives
├── mix.exs --> This is where you specify the dependencies, details of our project.
└── test
    ├── cards_test.exs
    └── test_helper.exs
```

2. Compile a project
3. Perform tasks on project. Such as documentation
4. Manage dependencies for project

- Tool for creating, compliling and testing elixir projects, managing its dependencies and more.
```
mix new first_app
cd first_app
iex -S mix

Erlang/OTP 21 [erts-10.1.1] [source] [64-bit] [smp:8:8] [ds:8:8:10] [async-threads:1] [hipe] [dtrace]

Interactive Elixir (1.7.4) - press Ctrl+C to exit (type h() ENTER for help)
```

- Adding dependency for a project can be done by editing deps section of mix.exs file:
```
 defp deps do
    [
      # {:dep_from_hexpm, "~> 0.3.0"},
      # {:dep_from_git, git: "https://github.com/elixir-lang/my_dep.git", tag: "0.1.0"},
      {:ex_doc, "~> 0.12"}
    ]
  end

```
- This is essentially array of tuples with first value of tuple at atom naming the dependecy and second value the version. ~> is important to specify.
- To install the dependency, run mix deps.get

### iex : (IEx shell)
- iex -S mix : To start a shell
- note: the first line in the iex shows that elixir runs on top of erlang vm
- Exit from shell: ctrl + c and then a
- Getting help: h() . Here you are calling a funtion h with no variables. This funtion will retrun :ok
- pwd()
- cd ".." or cd "/user/vinlok/" (note, you need to provide the path in quotes)
- ls()


**Compiling Code**
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