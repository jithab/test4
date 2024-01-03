---
layout: page
title: Abi Perwad
permalink: /abi/
---

<ul>
{% for post in site.categories.abi %}
  <li>
    <a href="{{ post.url }}"><h3>{{ post.title }}</h3></a>
    {{ post.date | date: "%B %d, %Y" }}
  </li>
{% endfor %}
</ul>
