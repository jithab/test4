---
layout: page
title: Auto Words
permalink: /auto-words/
---
<ul>
{% for post in site.categories.auto-words %}
  <li>
    <a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
    <!--{{ post.date | date: "%B %d, %Y" }}-->
  </li>
{% endfor %}
</ul>
