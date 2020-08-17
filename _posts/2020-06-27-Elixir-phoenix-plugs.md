---
layout: post
title: "Elixir Phoenix : Plugs"
date: 2020-06-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Plugs in Elixir are building blocks for code. Almost entire Phoenix works on plugs

<!--more-->

- Plugs are of two types:
1. Function Plugs: These are functions which accept conn object and return a conn object. Use this if this is to be shared in single controller.
2. Module Plugs: These are module which has init and call functions. 
    - Call function should return conn object. Use this if this plug is to be shared accross diffrent controllers.
    - init function is called only one time when the application initializes or starts.
    - call function is called everytime a request is made to the application.


## Writing a module Plug
- Create a directory named plugs in the controllers directory.
- Create a new .ex file with content as :

```
defmodule Discuss.Plugs.SetUser do
  import plug.Conn
  import Phoenix.Controller

  alias Discuss.Repo
  alias Discuss.User

  def init(_params) do
    # place code that needs to be run one time. Probably expensive code that needs to be loaded.
  end

  def call(conn, _params) do
    
  end

end
```

- Here, the _params to call function is what is returned from the init function.

# Defining plug in application

- This is done in router.ex
- Router.ex has two pipelines:
1. Browser pipleine (for html requests)
2. Api pipeline (for api requests)

``` 
pipeline :browser do
    plug Ueberauth
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

pipeline :api do
    plug :accepts, ["json"]
end

```

- to add the module plug we created, you have to use the complete module name as below

```
 pipeline :browser do
    plug Ueberauth
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
    plug Discuss.Plugs.SetUser
  end
```


