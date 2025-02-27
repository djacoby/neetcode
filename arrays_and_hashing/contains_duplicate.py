"""
Contains Duplicate

Leetcode 217 - https://leetcode.com/problems/contains-duplicate/

Time Complexity - O(n)
Space Complexity - O(n)

"""

from typing import List
from utils import LeetTester

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums)) < len(nums)

tester = LeetTester()
solution = Solution()

tester.test(True, solution.containsDuplicate([1, 2, 3, 1]))
tester.test(False, solution.containsDuplicate([1, 2, 3, 4]))
tester.test(True, solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

tester.summary()
