"""
Longest Common Prefix

Leetcode 14 - https://leetcode.com/problems/longest-common-prefix/

Time Complexity - O(n * min(m))
Space Complexity - O(1)

Solution: Vertical Scanning

Explanation:
- If an empty array is passed, return an empty string
- Iterate over the characters in the first string of the array
    - Compare each character with the character of the same index of the other strings
    - If a mismatch is found or a string is too short, return the prefix found so far
    - If no mismatch is found, return the entire first string

"""

from typing import List
from utils import LeetTester

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]

# Example test cases
tester = LeetTester()
solution = Solution()

tester.test("fl", solution.longestCommonPrefix(["flower", "flow", "flight"]))
tester.test("", solution.longestCommonPrefix(["dog","racecar","car"]))

tester.summary()