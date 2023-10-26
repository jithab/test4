---
layout: page
title: The English
permalink: /the-english/
---
<ul>
{% for post in site.categories.the-english %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <!--{{ post.date | date: "%B %d, %Y" }}-->
  </li>
{% endfor %}
</ul>
