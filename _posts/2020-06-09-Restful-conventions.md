---
layout: post
title: "Restful convenstions"
date: 2020-06-03
excerpt_separator: <!--more-->
categories: ['Web Development']
---


While developing a new web app, always first model business intent to user action and then back to code.

<!--more-->

Use the following table to outline intent, actions and code (cotroller in case of elixir)

| Intent | Action (path in router.ex) | Controller Function Name |
|-------|:------:|:------------------------:|
| See the form to create a new topic | GET /topics/new | new |
| Submit the form to create a topic | POST /topics/ | create |
| Get a list of all topics | GET Topics | index |
| Delete a topic with ID of 12 | DELETE /topics/12 | delete |
| see the form to update an existing topic with ID of 12 | GET /topics/12/edit | edit |
| Submit the form to update a topic with ID 12 | PUT /topics/12 | update|


