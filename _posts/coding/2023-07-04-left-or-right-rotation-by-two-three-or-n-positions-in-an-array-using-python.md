---
layout: post
title: "Left or Right rotation by two, three or N positions in an array using Python"
date: 2023-08-22 12:38:21 +0530
categories: interview python coding
type: coding
---
- **Input**: [1, 2, 3, 4, 5, 6, 7, 8, 9]
- **Output Left shift by 4**: [5, 6, 7, 8, 9, 1, 2, 3, 4]
- **Output Right shift by 5**: [5, 6, 7, 8, 9, 1, 2, 3, 4]
<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: Left shift by 4 and Right shift by 5
{% highlight python %}
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
left_shifts = 4
right_shifts = 5

left = data[left_shifts:]+ data[:left_shifts]
right = data[-right_shifts:]+ data[:-right_shifts]

print("left: ", left)
print("right: ", right)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>
- **Interviewer**: Left shift by 4 without slicing
{% highlight python %}
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shifts = 4

for shift in range(shifts):
    swap = data[0]
    for index in range(len(data)-1):
        data[index] = data[index+1]
    data[-1] = swap

print(data)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>

- **Interviewer**: Right shift by 5 without slicing
{% highlight python %}
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shifts = 5

for shift in range(shifts):
    swap = data[-1]
    for index in range(len(data)-1, 0, -1):
        data[index] = data[index-1]
    data[0] = swap

print(data)
{% endhighlight %}
<p>&nbsp;</p><hr/><p>&nbsp;</p>