"""
Majority  Element

Leetcode 169 - https://leetcode.com/problems/majority--element/

Time Complexity - 0(n)
Space Complexity - 0(n)

Solution: Hash Map

Explanation:
- Create a hashmap to track occurences of a number
- Create a variable to return the result
- Create a variable to track the highest frequency count
- Iterate over each number in the list nums:
    - For each number, increase its count in the count dictionary
    - Check if the count of the current number exceeds the current maxCount
    - If count of the current number exceeds the current maxCount
        - Update res to the current number and update maxCount to the new highest count.
- Return the number stored in res, which is the most frequent number in the list

* Also listed is a Boyer Moore voting algorithm implementation which is more space efficient

"""

from utils import LeetTester
from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res

    def boyerMooreVoting(self, nums: List[int]) -> int:
        res = 0
        maxCount = 0

        for num in nums:
            if maxCount == 0:
                res = num
            maxCount += (1 if num == res else -1)
        return res

# Example test cases
tester = LeetTester()
solution = Solution()

tester.test(3, solution.majorityElement([3, 2, 3]))
tester.test(2, solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))

tester.summary()
