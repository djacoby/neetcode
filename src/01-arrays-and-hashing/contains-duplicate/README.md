# Contains Duplicate

**Difficulty:** Easy

## Problem

Given an integer array `nums`, return `true` if any value appears **more than once** in the array, otherwise return `false`.

## Examples

### Example 1:

**Input:** `nums = [1, 2, 3, 3]`

**Output:** `true`

### Example 2:

**Input:** `nums = [1, 2, 3, 4]`

**Output:** `false`

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Solution

By converting the array to a Set, which only stores unique values, we remove all duplicates. If the size of the set is less than the length of the original array, we know the array contained duplicate values.

## Time & Space Complexity

- Time complexity: O(n) O(n)
- Space complexity: O(n) O(n)
