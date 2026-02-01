"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/
"""

# ---------- STARTER CODE ----------

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        for i, n in enumerate(nums):
            if target - n in mapping:
                return [i, mapping[target-n]]
            mapping[n] = i
        return []
