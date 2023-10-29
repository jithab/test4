---
layout: page
title: Most Common Words
permalink: /most-common-words/
---
<ul>
{% assign sorted_data = site.categories.auto-words | sort:'title' %}
{% for post in sorted_data %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>

<style type="text/css"> 
  li { display:inline; margin-right: 1em; }
  li:before { content:"• "; }       
</style>