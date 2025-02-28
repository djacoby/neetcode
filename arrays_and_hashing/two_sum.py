"""
Two Sum

Leetcode 1 - https://leetcode.com/problems/two-sum/

Time Complexity - 0(n) 
Space Complexity - 0(n) 

Solution: Hash Map

Explanation:

- Create a dictionary to store the value and index of the numbers in the list
- Iterate through the list and calculate the difference between the target and the current number
- If the difference is in the dictionary, return the index of the difference and the current index
- Otherwise, add the current number and index to the dictionary

"""

from typing import List
from utils import LeetTester

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # val -> index

        for i, num in enumerate(nums):
          difference = target - num
          if difference in numMap:
              return [numMap[difference], i]
          numMap[num] = i

# Example test cases
tester = LeetTester()
solution = Solution()

tester.test([0, 1], solution.twoSum([2, 7, 11, 15], 9))
tester.test([1, 2], solution.twoSum([3, 2, 4], 6))
tester.test([0, 1], solution.twoSum([3, 3], 6))

tester.summary()