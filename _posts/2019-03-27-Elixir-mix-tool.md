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

