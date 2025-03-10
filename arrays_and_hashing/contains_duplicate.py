"""
Contains Duplicate

Leetcode 217 - https://leetcode.com/problems/contains-duplicate/

Time Complexity - O(n)
Space Complexity - O(n)

Solution: Hash Set Length

Explanation:

- Convert the list to a set and compare the length of the set to the length of the list
- If the length of the set is less than the length of the list, return True
- Otherwise, return False

"""

from typing import List
from utils import LeetTester

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums)) < len(nums)

# Example test cases
tester = LeetTester()
solution = Solution()

tester.test(True, solution.containsDuplicate([1, 2, 3, 1]))
tester.test(False, solution.containsDuplicate([1, 2, 3, 4]))
tester.test(True, solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

tester.summary()
