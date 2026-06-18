# Two Sum

**Difficulty:** Easy

## Problem

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

## Examples

### Example 1:

**Input:** nums = [3,4,5,6], target = 7

**Output:** Output: [0,1]

### Example 2:

**Input:** nums = [4,5,6], target = 10

**Output:** Output: [0,2]

### Example 3:

**Input:** nums = [5,5], target = 10

**Output:** Output: [0,1]

## Constraints

- `2 <= nums.length <= 1000`
- `10,000,000 <= nums[i] <= 10,000,000`
- `10,000,000 <= target <= 10,000,000`
- Only one valid answer exists. 

## Solution

Create a map where the key is the difference (target - x) and the value is the index where the calculation was made. Iterate over the array and calculate the difference of the target and the current value (difference = target - x). Check if the "complement" value (x) exists in the map, if so return [complement, i], otherwise add the difference to the map.

## Time & Space Complexity

- Time complexity: O(n)
- Space complexity: O(n)