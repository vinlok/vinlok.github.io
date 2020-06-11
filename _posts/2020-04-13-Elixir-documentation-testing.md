---
layout: post
title: "Elixir Documentation and testing"
date: 2020-03-27
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Using the elixir doc module, you can generate fancy documentation for the code you right.

<!--more-->

## Adding Documentation
- Add :ex_doc to the your project dependency. Refer to Elixir Tools documentation for the steps.
- Install the :ex_doc module.
- Documentation can be done at two levels:
1. At the module,
    - add @moduledoc """ """
2. At function level:
    - add @doc above the function
    Example:
    ```
    """
    This function does bla and needs this argument `some_arg`
    ## Examples
        iex> deck = Cards.Create

    """
   ```
3. Then run : mix docs. This will create an docs/index.html with the comment you have added to the code. This is how the official documentation of elixir is also mantained.
4. Adding example in function doc needs "## ". Also, the actual example should be indented with three spaces.


## Writing Tests
- Testing in Elixir is first class citizen, it is self contained. You do not have to load any additional libraries. All batteries included.

- When you generate the mix project, it create the "test" directory. It contains: {module}_test and test_helper.exs
- To run the test, do
```
mix test
```
### Classification of Elixir tests
1. Tests in Elixir can be classified into three categories:
2. Single Assertion test. Example:
    ```
    test "the truth" do
    assert 1 + 1 == 2
    end
    ```
3. doctest:
    - These are pulled directly from the documentation you do. Example:
    ```
        @doc """
      Deals the decks. needs `hand_size`
    
      ## Examples
            iex> deck = Cards.create_deck
            iex> {hand,deck} = Cards.deal(deck,1)
            iex> hand
            ["Ace of Spades"]
      """
    ```
    - If you have added an example to your documentation like above, running the doctest will actuall execute the commands as if they were on elixir shell. And, it will even make sure that the output matches with ["Ace of Spades"] here.
    - It is always helpful to run the actual code in the shell and then copy the output as examples.
    - All the lines without iex> as prefix are nothing but assertions. This is how you can make multiple assertions.

4. Test case assertions:
    Example:
    ```
      test "Cards create deck return 20 cards(deck with 20 cards" do
        deck_length = length(Cards.create_deck)
        assert deck_length == 20
      end
    
      test "Shuffle method indeed shuffle the content" do
        deck = Cards.create_deck
        assert deck != Cards.shuffle(deck)
      end
    
      #or
    
      test "Shuffle method indeed shuffle the content" do
        deck = Cards.create_deck
        refute deck != Cards.shuffle(deck)
      end
    ```
    Note the use of refute.


