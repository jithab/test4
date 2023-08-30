---
layout: page
title: Englishified
permalink: /englishified/
---
<ul>
{% for post in site.categories.englishified %}
  <li>
    <a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
    <!--{{ post.date | date: "%B %d, %Y" }}-->
  </li>
{% endfor %}
</ul>