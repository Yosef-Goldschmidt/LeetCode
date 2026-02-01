# Problem link: https://leetcode.com/problems/valid-anagram
# ---------- DESCRIPTION ----------
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. count the letters in each word
        #2. compare and check if the freqency is equal
        return Counter(s) == Counter(t)









