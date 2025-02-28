"""
Valid Anagram

Leetcode 242 - https://leetcode.com/problems/valid-anagram/

Time Complexity - O(n + m)
Space Complexity - O(n)

Solution: Frequency Array

Explanation:
- Create a frequency array of size 26 to store the frequency of each letter in the alphabet
- Iterate through the first string and increment the frequency of each letter
- Iterate through the second string and decrement the frequency of each letter
- If the frequency array contains any non-zero values, return False
- Otherwise, return True

"""

from utils import LeetTester

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # initalize frequency array for characters in the alphabet
        frequency_array = [0] * 26

        for i in range(len(s)):
            frequency_array[ord(s[i]) - ord('a')] += 1 # increment occurences of letter in string s
            frequency_array[ord(t[i]) - ord('a')] -= 1 # decrement occurences of letter in string t

        for val in frequency_array:
            if val != 0:
              return False

        return True

# Example test cases
tester = LeetTester()
solution = Solution()

tester.test(True, solution.isAnagram("anagram", "nagaram"))
tester.test(False, solution.isAnagram("rat", "car"))

tester.summary()