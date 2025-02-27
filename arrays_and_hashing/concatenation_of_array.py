"""
Concatenation of Array

Leetcode 1929 - https://leetcode.com/problems/concatenation-of-array/

Time Complexity - O(n)
Space Complexity - O(n)

"""
from utils import LeetTester

def get_concatenation(nums):
    length = len(nums)
    result = [0] * (2 * length)  # Initialize an array of size 2 * length

    for i in range(length):
        result[i] = result[i + length] = nums[i]

    return result

tester = LeetTester()

tester.test([1, 2, 1, 1, 2, 1], get_concatenation([1, 2, 1]), '[1, 2, 1]')
tester.test([1, 3, 2, 1, 1, 3, 2, 1], get_concatenation([1, 3, 2, 1]), '[1, 3, 2, 1]')

tester.summary()
