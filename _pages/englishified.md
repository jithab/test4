---
layout: page
title: Englishified
permalink: /englishified/
---

{% for post in site.categories.englishified %}
<h2>{{ post.title }}</h2>
<time>{{ post.date }}</time>
{% endfor %}