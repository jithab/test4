---
layout: page
title: Usage and Example
permalink: /usage-and-example/
categories: [
	["Coordinating Conjunction", [
		["for", "For"],
		["and", "And"],
		["nor", "Nor"],
		["but", "But"],
		["or", "Or"],				
		["yet", "Yet"],	
		["so", "So"]		
	]],
		["Frequency Adverbs", [
		["barely", "Barely"],
		["hardly", "Hardly"],
		["seldom", "Seldom"],
		["scarcely", "Scarcely"],
		["rarely", "Rarely"],				
		["ever", "Ever"]	
	]],
	["Punctuations", [
		["colon", "Colon"],
		["semicolon","Semicolon"],
		["square-bracket", "Square Bracket"]
	]],
	["Symbols", [
		["dollar", "Dollar"],
		["euro", "Euro"],
		["pound", "pound"]
	]]]
---

<div>
{% for category in page.categories %}
  <h4>{{ category[0] }}</h4>
  <ul>
    {% for page in category[1] %}
      <li><a href="/{{ page[0] }}">{{ page[1] }}</a></li>
    {% endfor %}
  </ul>	  
{% endfor %}
</div>

<h4>All</h4>
<ul>
{% for post in site.categories.the-english %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <!--{{ post.date | date: "%B %d, %Y" }}-->
  </li>
{% endfor %}
</ul>
{% comment %}
<p>&nbsp;</p>
<p>See <a href="/most-common-words">Most Common Words</a></p>

<p>&nbsp;</p>
<p>See <a href="/phrasal-verbs">Phrasal Verbs</a></p>
{% endcomment %}
<p>&nbsp;</p>
<p>See <a href="/x-versus-y">Word1 versus Word2</a></p>
<style type="text/css"> 
  li { display:inline; margin-right: 1em; }
  li:before { content:"• "; }       
</style>
