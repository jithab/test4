---
layout: page
title: Phrasal Verbs
permalink: /phrasal-verbs/
---
<ul>
{% assign sorted_data = site.categories.auto-phrasalverbs | sort:'title' %}
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
