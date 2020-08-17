---
layout: post
title: "Elixir Phoenix Forms and templates"
date: 2020-05-31
excerpt_separator: <!--more-->
categories: ['Elixir']
---

Phonenix is a webframework. Its job is to act as a web server. Used generally to serve HTML, JSON, websockets.

<!--more-->

### Forms
- Elixir provides a special function named form_for to handle HTML forms.
- Consider the following form in EEX template:
```
1 <%= form_for @changeset, topic_path(@conn, :create), fn f -> %>
2  <div class="form-group">
3    <%= text_input f, :title, placeholder: "Title", class: "form-control" %>
4 </div>
5  <%= submit "Save Topic", class: "btn btn-primary" %>
6 <% end %>
```

- Here the code between <%= > brackets encapsulates the elixir code. The above can be converted to following elixir code:
```
 form_for(@changeset, topic_path(@conn, :create), fn f -> end) #This is elixir code for above.
```

- This form is called from the controller module as below:
```
def new(conn, _params) do
    changeset = Topic.changeset(%Topic{}, %{})

    render conn, "new.html", changeset: changeset #this is keywork list You can pass any variable. Example, you can say sum = 1 + 1 and pass sum: sum to template
  end
```
- Whatever is written between <%= and %> is coverted to elixir code by EEX template.
You can say <%= 1 + 1 %> and that will be shown on the html page or put code to do conditional rendering. Example, show a given button based on code.

- Lets decode the above template line by line:

- Line 1: This line can be read as using the form_for function with Changeset is input, whenver user submits the form, send him to topic_path with  conn as attribute and create function using POST. changeset is a mandatory input for the form_for function.

- When you are calling the render in elixir code, you are passing changeset as variable. This way you can pass any thing to be rendered dynamically to the form.

- Line 3: Here, the form is represented as function f, to which we are adding text_input with title placeholder. This is the anonymous function

## Path helpers in Phoenix
- For line one, the topic_path is resoved into the location of the form.
- Lets see what is topic path. Run the following command:
```
mix phoenix.routes

page_path  GET   /            Discuss.PageController :index
topic_path  GET   /topics/new  Discuss.TopicController :new
topic_path  POST  /topics      Discuss.TopicController :create
```
- The first column is general_name of path. It is of the format ControllerName_path.
- The Second and third column tells the URL for the path.
- Thus,topic_path can accept a GET request on /topics/new and it will be redirected to Discuss.TopicController :new
- Hence whenever the user submits the form, he will be sent to route resolved by topic_path(@conn, :create) as below:
    get a reference for topic_path with :create function which will be: /topics with POST. If you go to the router.ex, you will see :
    post "/topics", TopicController, :create

- Instead of writing post /topics, we reference using topic patch and then we can keep changing the urls only at one place which is router.ex

## Anchor tag vs link to for hyperlinking
- You can specify anchor tag as below:
```
 <a class="btn-floating btn-large waves-effect waves-light red " href="<%= topic_path(@conn, :new) %>">
 ```
 - This can be also replaced with "link to" function in elixir as below:

 ```
 <%= link to: topic_path(@conn, :new), class: "btn-floating btn-large waves-effect waves-light red " do %>
    <i class="material-icons">add</i>
    <% end %>
 ```
- Link helper function allows use to specify the method for the rest call. The anchor tag <a> by default does a get request.

```
<%= link "Delete", to: topic_path(@conn, :delete, topic), method: :delete %>
```

-