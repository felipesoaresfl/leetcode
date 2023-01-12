'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Explanation:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    There are 4 good pairs (0,3), (0,4), (3,4), (2,5).

https://leetcode.com/problems/number-of-good-pairs/description/
'''


class Solution:
    def numIdenticalPairs(nums):
        count_numbers = {}
        pairs = 0
        for num in nums:
            if num in count_numbers:
                pairs += count_numbers[num]
                count_numbers[num] += 1
            else:
                count_numbers[num] = 1
        return pairs
    print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
