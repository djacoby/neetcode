"""
Concatenation of Array

Leetcode 1929 - https://leetcode.com/problems/concatenation-of-array/

Time Complexity - O(n)
Space Complexity - O(n)

"""

from typing import List
from utils import LeetTester

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * (2 * length)  # Initialize an array of size 2 * length

        for i in range(length):
            result[i] = result[i + length] = nums[i]

        return result

# Example test cases
tester = LeetTester()
solution = Solution()

tester.test([1, 2, 1, 1, 2, 1], solution.getConcatenation([1, 2, 1]))
tester.test([1, 3, 2, 1, 1, 3, 2, 1], solution.getConcatenation([1, 3, 2, 1]))

tester.summary()