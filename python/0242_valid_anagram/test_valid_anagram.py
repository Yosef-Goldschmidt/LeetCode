# ------- Pytest unit tests for LC 0217 - Contains Duplicate -------

from valid_anagram import Solution

def test_is_anagram():
    s = Solution()
    #assert s.isAnagram("", "") is True
    assert s.isAnagram("a", "b") is False
    assert s.isAnagram("a", "aa") is False
    assert s.isAnagram("abc", "bca") is True
    assert s.isAnagram("a", "a") is True

