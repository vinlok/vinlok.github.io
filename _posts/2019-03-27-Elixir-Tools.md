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
Mix tool is installed default during the elixir installation on Mac using Brew. Mix can be used for:

1.  Create a new project
    ```
    mix new <projet name>
    ```
    This will create template files as below:
```
.
├── README.md
├── config
│   └── config.exs
├── lib
│   └── cards.ex --> This is where the code lives
├── mix.exs
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

### iex : (IEx shell)
- note: the first line in the iex shows that elixir runs on top of erlang vm
- Exit from shell: ctrl + c and then a
- Getting help: h() . Here you are calling a funtion h with no variables. This funtion will retrun :ok
- pwd()
- cd ".." or cd "/user/vinlok/" (note, you need to provide the path in quotes)
- ls()

