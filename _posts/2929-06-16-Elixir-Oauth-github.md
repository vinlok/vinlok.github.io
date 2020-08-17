---
layout: post
title: "Elixir Phoenix Github based Oauth Authentication"
date: 2020-06-16
excerpt_separator: <!--more-->
categories: ['Elixir']
---

https://github.com/ueberauth/ueberauth is the mechanism used by Phoenix to setup Oauth based mechanism in Phoenix.
<!--more-->

## Steps to setup uberauth
1. Add dependencies for ueberauth and ueberauth_github in mix.deps
```
 defp deps do
    [{:phoenix, "~> 1.2.5"},
     {:phoenix_pubsub, "~> 1.0"},
     {:phoenix_ecto, "~> 3.0"},
     {:postgrex, ">= 0.0.0"},
     {:phoenix_html, "~> 2.6"},
     {:phoenix_live_reload, "~> 1.0", only: :dev},
     {:gettext, "~> 0.11"},
     {:cowboy, "~> 1.0"},
     {:ueberauth, "~> 0.3"},
     {:ueberauth_github, "~> 0.4"}]

  end
```
2. Add ueberauth and ueberauth_github to application section for initialization when phoenix starts.
```
 def application do
    [mod: {Discuss, []},
     applications: [:phoenix, :phoenix_pubsub, :phoenix_html, :cowboy, :logger, :gettext,
                    :phoenix_ecto, :postgrex, :ueberauth, :ueberauth_github]]
  end
```

3. Install the dependencies:
```
mix depts.get
```

4. In github.com, under settings -> Developer Settings -> Oauth Apps, create a new application. Enter Authorization Callback URL. This is the URL what github will redirect the user back to upon successfull authentication. For ueberauth github module, it is /auth/github/callback.

5. This will create the clientID (Your application ID), generate the client Secret.

6. In config/config.exs, add the following:
```
config :ueberauth, Ueberauth,
providers: [
github: {Ueberauth.Strategy.Github, [default_scope: "user,public_repo,notifications"]}
]
- Here we define the stragy for the git hub provide. When the request is sent to gihub, user information (email, name), public repo list, notification is sent back

config :ueberauth, Ueberauth.Strategy.Github.OAuth,
 client_id: "1bd379c2bcd4d53b3324",
 client_secret: "c580xxxxxxxxxxxxxxxxxxxxxxxxxxx"
 ```
- Here, we define that we are using the github provider of uberauth.

7. Create a module named auth_controller (name of the module can be anything). In this module, you need to define a function name callback. This is the function invoked when the user is redirected back from github:

```
defmodule Discuss.AuthController do
  use Discuss.web, :controller
  plug Ueberauth

  def callback(conn, params) do
    IO.puts "conns ++++++++++++"
    IO.inspect(conn)
    IO.puts "params ++++++++++++"
    IO.inspect(params)
    IO.puts "++++++++++++"

  end
end
```
8. Now, define the routes in the router.exs for auth controller.:

```
 scope "/auth", Discuss do
    pipe_through :browser

   get "/:provider", AuthController, :request # extract provider from params. The request
   get "/:provider/callback", AuthController, :callback
  end
```