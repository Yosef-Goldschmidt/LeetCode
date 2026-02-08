"""
LeetCode 271: Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/
"""

# ---------- STARTER CODE ----------

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += f"{len(w)}#{w}"

        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        w_len = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c == '#':
                strs.append(s[i + 1:i + 1 + int(w_len)])
                i += 1 + int(w_len)
                w_len = ""
            else:
                w_len += c
                i += 1
        return strs



