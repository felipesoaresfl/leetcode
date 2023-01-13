/*
Given an integer array nums, return the maximum difference between two
successive elements in its sorted form. If the array contains less than two elements,
return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9)
has the maximum difference 3.

https://leetcode.com/problems/maximum-gap/
*/

const maximumGap = function(nums) {
    let list = []
    let numbers = nums.sort((a,b) => a - b)
    if (numbers.length < 2) return 0
    
    for (var i = 0; i < (numbers.length); i++){
        if (numbers[i+1]){
            let result = numbers[i+1] - numbers[i]
            list.push(result)
        }
    }
    return Math.max.apply(0, list)
};

console.log(maximumGap([3,6,9,1]))