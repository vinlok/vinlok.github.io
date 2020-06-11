---
layout: post
title: "Elixir Pipe Operator ( |> )"
date: 2020-04-08
excerpt_separator: <!--more-->
categories: ['Elixir']
---

The Pipe operator : |> is used in Elixir to pass output of one functionto other

<!--more-->

- |> operator is similar to | of unix.
- Example code:

```
 def create_deck do
    values = ["Ace","Two","Three","Four","Five"]
    suits = ["Spades","Clubs","Hearts","Diamonds"]

    for value <- values, suit <- suits do
      [value,suit]
      "#{value} of #{suit}"
    end
  end

  def shuffle(deck) do # Here deck is the variable you pass to it.
    Enum.shuffle(deck)
  end

  def deal(deck, hand_size) do
    Enum.split(deck,hand_size)
  end

  def create_hand(hand_size) do
    Cards.create_deck
    |> Cards.shuffle
    |> Cards.deal(hand_size)
  end

```

- Here create_hand function is calling create_deck whose output is fed as input to suffle. shuffle take one argument and the output from first function is assigned to this variable.
- Now the output of shuffle is sent to deal which take two argument. Again, output is assigned to first variable which is deck here.
- Thus you need to have very consistent first arguments when you are using pipeline operator.