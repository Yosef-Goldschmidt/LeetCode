# ------- Pytest unit tests for LC 0217 - Contains Duplicate -------

from solution import Solution

def test_contains_duplicate():
    s = Solution()
    assert s.containsDuplicate([1,2,4,5,2]) is True
    assert s.containsDuplicate([1]) is False
    assert s.containsDuplicate([1,2,3]) is False
    assert s.containsDuplicate([]) is False
    assert s.containsDuplicate([-1, -1]) is True

