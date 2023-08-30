---
layout: page
title: Coding
permalink: /coding/
---

{% for post in site.categories.coding %}
<h2>{{ post.title }}</h2>
<time>{{ post.date }}</time>
{% endfor %}