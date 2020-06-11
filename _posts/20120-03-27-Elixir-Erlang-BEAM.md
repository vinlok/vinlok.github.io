---
layout: post
title: "Elixir-Erlang-BEAM-Relationship"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Elixir is a dynamic, functional language designed for building scalable and maintainable applications.

<!--more-->
# Relationshipt between Elixir->Erlang->BEAM

Elixir leverages the Erlang VM, known for running low-latency, distributed and fault-tolerant systems, while also being successfully used in web development and the embedded software domain.

Elixir runs on top of Erlang VM, thus, you need to install Erlang before you can run elixir.

Erlang is a separate language created for Telephone systems in 1970's. It is notoriously known for its cryptic syntax and symbols.

Thus, to simplify syntax of Erlang, Elixir was developed. 

Erlang runs on top of BEAM. Bogdan's Erlang Abstract Machine. It is similar to what we have in Java world -> JVM.

Code --> Elixir --> Code is converted to Erlang --> Compiled and Executed by BEAM.

#Coding patterns
- Writing code in Elixir requries discipline. Example, when using |> operator, you need to be consistent in use of first argument. This is because the first arugument is default arg to which functions pass values.

