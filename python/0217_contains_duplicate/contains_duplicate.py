# Problem link: https://leetcode.com/problems/contains-duplicate
# ---------- DESCRIPTION ----------
# Given an integer array nums, return true
# if any value appears at least twice in the array,
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #1.Set holds only unique values.
        #  By checking set length we can see if there are duplicates.
        return len(nums) != len(set(nums))







