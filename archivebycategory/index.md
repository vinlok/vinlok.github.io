---
layout: default
title: Post by Category
permalink: /categoryview/
sitemap: false
---
<div style="margin-left:auto;margin-right:auto;width:60%;">
    {% assign categories = site.categories | sort %}
    {% for category in categories %}
        <span class="site-tag">
            <a href="#{{ category | first | slugify }}">
                    {{ category[0] | replace:'-', ' ' }} ({{ category | last | size }})
            </a>
        </span>
    {% endfor %}
</div>

<div id="index" style="margin-left:auto;margin-right:auto;width:60%;">
    {% for category in categories %}
        <a name="{{ category[0] }}"></a>
        <h3>{{ category[0] | replace:'-', ' ' }}</h3>
        {% assign sorted_posts = site.posts | sort: 'title' %}
        {% for post in sorted_posts %}
            {%if post.categories contains category[0]%}
                <li style="margin-left:auto;margin-right:auto;width:90%;">
                <h4>
                    <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="{{ post.title }}">{{ post.title }} 
                    </a>
                </h4>
                <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
            </li>
            {%endif%}
        {% endfor %}
    {% endfor %}
</div>
