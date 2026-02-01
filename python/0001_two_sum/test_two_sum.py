import pytest
from two_sum import Solution


def test_basic_case():
    sol = Solution()
    assert set(sol.twoSum([2,9,8,7,4], 9)) == {0,3}
    assert set(sol.twoSum([1,2], 3)) == {0,1}
    assert sol.twoSum([1,2], 4) == []
    #pytest.fail("Test not implemented yet")

def test_edge_case():
    sol = Solution()
    assert sol.twoSum([], 0) == []
    assert sol.twoSum([1,1,1,1,1,1,1], 1) == []
