"""
Group Anagrams

Leetcode 49 - https://leetcode.com/problems/group-anagrams/

Time Complexity - O(m * n)
Space Complexity - 0(m)

Solution:

Explanation:
- Create a default dict to avoid key errors when checking for keys
- Iterate over each string in the list
    - For each string create a frequency array
    - Add/ update anagrams to groupMap with the frequency array as a tuple as the key
        - note: the frequency array needs converted to a tuple because lists are mutable therefore cannot be a dict key
- Return an array from the map values

"""

from typing import List
from collections import defaultdict
from utils import LeetTester

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            groupMap[tuple(count)].append(s)

        return list(groupMap.values())

# Example test cases
test_1 = {
    "input": ["eat","tea","tan","ate","nat","bat"],
    "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
}

test_2 = {
    "input": [""],
    "expected": [[""]] 
}

test_3 = {
    "input": ["a"],
    "expected": [["a"]]
}

tester = LeetTester()
solution = Solution()

tester.test(test_1["expected"], solution.groupAnagrams(test_1["input"]))
tester.test(test_2["expected"], solution.groupAnagrams(test_2["input"]))
tester.test(test_3["expected"], solution.groupAnagrams(test_3["input"]))

tester.summary()
