---
layout: post
title:  Minimum Window Substring
date:   2023-12-18 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
def min_window(s, t):
    tset = {}
    for char in t:
        tset[char] = tset.get(char, 0) + 1

    t_len = len(t)
    s_len = len(s)
    min_len = s_len + 1
    min_index = 0
    left_pointer = 0
    valid_chars_count = 0

    for right_pointer in range(s_len):
        char = s[right_pointer]
        if char not in tset:
            continue

        tset[char] -= 1
        if tset[char] >= 0:
            valid_chars_count += 1
        if valid_chars_count != t_len:
            continue

        # increase the left_pointer if possible
        while True:
            if s[left_pointer] in tset:
                if tset[s[left_pointer]] == 0:
                    break
                tset[s[left_pointer]] += 1
            left_pointer += 1

        new_min_len = right_pointer - left_pointer + 1
        if new_min_len < min_len:
            min_len = new_min_len
            min_index = left_pointer

    return "" if min_len > s_len else s[min_index:min_index + min_len]
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")


pr("BANC" == min_window("ADOBECODEBANC", "ABC"))
pr("a" == min_window("a", "a"))
pr("" == min_window("a", "aa"))
{% endhighlight %}