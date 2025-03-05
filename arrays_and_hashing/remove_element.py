"""
Remove Element

Leetcode 27 - https://leetcode.com/problems/remove-element/

Time Complexity - 0(n)
Space Complexity - 0(1)

Solution: Two Pointers

Explanation:
- Initialize a pointer to the new array length
- Iterate through the array
    - If the number does not equal equal the target
        - Set the value of the array at the pointer to the number
        - Increment the pointer
- Return the pointer

Essentially we keep the numbers that aren't the target value and ignore the ones that are.
Shift the kept numbers to the front of the list.
At the end, return how many numbers were kept.

"""

from utils import LeetTester
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arrPointer = 0  # Pointer for the new array length
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[arrPointer] = nums[i]  # Overwrite the element in place
                arrPointer += 1  # Move the pointer forward

        return arrPointer  # The new length of the array

# Example test cases
tester = LeetTester()
solution = Solution()

tester.test(2, solution.removeElement([3,2,2,3], 3))
tester.test(5, solution.removeElement([0,1,2,2,3,0,4,2], 2))

tester.summary()
