---
layout: default
title: Vinayak's Blog
---
  <h2 style="margin-left:auto;margin-right:auto;width:60%;">{{ page.title }}</h2>
  <ul class="posts">

    {% for post in site.posts reversed %}
      <li style="margin-left:auto;margin-right:auto;width:60%;"><a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
      <p>{{ post.excerpt }}</p>
      <a href="{{ post.url }}">Read more...</a>
      <hr> 
      </li>
    {% endfor %}
  </ul>