# Valid Anagram

**Difficulty:** Easy

## Problem

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Examples

### Example 1:

**Input:** `s = "racecar", t = "carrace"`

**Output:** `true`

### Example 1:

**Input:** `s = "jar", t = "jam"`

**Output:** `false`

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Solution

Return false if strings are of different length. Then create a a fixed size array of 26 zeros (for 26 letters in the alphabet). Iterate over the length of `s` and increment the index value of the given letter for `s`, decrement the value for `t`. Once the loop is complete we know `s` and `t` are valid anagrams.

## Time & Space Complexity

Time complexity: O (n + m)
Space complexity: O(1)
