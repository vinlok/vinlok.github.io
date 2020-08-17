---
layout: post
title: "Elixir Phoenix : websockets"
date: 2020-08-01
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Websockets in Phoenix provide a way for two way communication between client and server. It is a protocol used by phoenix to exchange live data between client and server.

<!--more-->

## Sockets
- Sockets in Phoenix are arrage into channels. Each channel has a specific resources doing specific thing.

- Concept in Sockets:
    - Join: Whenver a user initially connects join function is called.
    - Handel_in: When a browser initiate a communication, handle_in is called.

- Phoenix has server side implementation and client side implementation:
    - web/channels/user_socket.ex --> This is where we code server side sockets
    - web/static/js/socket.js --> This is where we code client side sockets.

### Server Side Sockets
web/channels/user_socket.ex : This is almost similar to router.ex file.com


```
defmodule Discuss.UserSocket do
  use Phoenix.Socket

  ## Channels
  channel "comments:*", Discuss.CommentsChannel  # The first argument is the name of the channel a client will be connecting to. Second argument is the module which is going to handle it.

  ## Transports
  transport :websocket, Phoenix.Transports.WebSocket

  def connect(_params, socket) do  #This is called whenever a client connenect to the server. The socket object here is similar to conn object in controller.
    {:ok, socket}
  end

  def id(_socket), do: nil
end
```

- Discuss.CommentsChannel is the module which is invoked everyting a client connects to comments channel.

```
defmodule Discuss.CommentsChannel do
  use Discuss.Web, :Channel # this imports all the functionality related to channel from phoenix.

  def join(name, _params, socket) do

  end

  def handle_in() do

  end
end
```

- Here join and handle_in are the callbacks function. These are the function automatically called when client connects.

- Join: 
```
  def join(name, _params, socket) do
    IO.puts("++++++++++++++++")
    IO.puts(name)
    {:ok,%{hey: "there"}, socket} # This is the return from join or rather a socket module expected by default.
  end
```
    - Join function is used for the first time communication.

- handle_in:
    - handle_in is used for the followup communication.


- Communication over websockets happen over JSON format. Poison is the Elixir library which converts content to JSON.

- In order to covert a data from database to JSON, you have to add @derive tag in the model file as below:

```
defmodule Discuss.Comment do
  use Discuss.Web, :model

  @derive {Poison.Encoder, only: [:content]} # this tells poison that only take the content and convert that to JSON

  schema "comments" do
    field :content, :string
    belongs_to :user, Discuss.User
    belongs_to :topic, Discuss.Topic
    timestamps()
  end

  def changeset(struct, params\\ %{})do
    struct
    |> cast(params, [:content])
    |> validate_required([:content])
  end

end
```


