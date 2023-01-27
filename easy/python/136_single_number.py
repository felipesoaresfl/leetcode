'''
Given a non-empty array of integers nums,
every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime
complexity and use only constant extra space.

https://leetcode.com/problems/single-number/description/
'''

from collections import Counter


class Solution:
    def singleNumber(nums):
        counter_numbers = Counter(nums)
        for number in nums:
            if counter_numbers[number] == 1:
                return number
    print(singleNumber([4, 1, 2, 1, 2]))
