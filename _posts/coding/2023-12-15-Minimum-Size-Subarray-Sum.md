---
layout: post
title:  Minimum Size Subarray Sum
date:   2023-12-15 12:34:56 +0000
categories: coding python
type: coding
---
{% highlight python %}
def subarray_length(target, nums):
    left_pointer = right_pointer = 0
    sum_of_nums = 0
    n = len(nums)
    min_len = n + 1
    while right_pointer < n:
        sum_of_nums += nums[right_pointer]
        while sum_of_nums >= target:
            min_len = min(min_len, right_pointer - left_pointer + 1)
            sum_of_nums -= nums[left_pointer]
            left_pointer += 1
        right_pointer += 1

    return min_len if min_len <= n else 0
{% endhighlight %}

{% highlight python %}
def pr(ok): print("Ok" if ok else "Error")


pr(2 == subarray_length(7, [2, 3, 1, 2, 4, 3]))
pr(1 == subarray_length(4, [1, 4, 4]))
pr(0 == subarray_length(11, [1, 1, 1, 1, 1, 1, 1, 1]))
{% endhighlight %}