import pytest
from typing import Optional, List
from invert_binary_tree import Solution


# Standard TreeNode definition as per LeetCode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a level-order list."""
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Helper function to convert a binary tree back to a level-order list for comparison."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Cleanup trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


@pytest.fixture
def sol():
    """Provides a fresh instance of the Solution class for each test."""
    return Solution()


def test_basic_inversion(sol):
    # Original: [4, 2, 7, 1, 3, 6, 9]
    input_list = [4, 2, 7, 1, 3, 6, 9]
    expected = [4, 7, 2, 9, 6, 3, 1]

    root = build_tree_from_list(input_list)
    inverted_root = sol.invertTree(root)
    assert tree_to_list(inverted_root) == expected


# to[4, 7, 2, 9, 6,

def test_empty_tree(sol):
    # Edge case: Empty tree should return None
    assert sol.invertTree(None) is None


def test_small_tree(sol):
    # Original: [2, 1, 3] -> Inverted: [2, 3, 1]
    root = build_tree_from_list([2, 1, 3])
    inverted = sol.invertTree(root)
    assert tree_to_list(inverted) == [2, 3, 1]


def test_single_node(sol):
    # Single node tree remains unchanged
    root = TreeNode(1)
    inverted = sol.invertTree(root)
    assert inverted.val == 1
    assert inverted.left is None and inverted.right is None


def test_asymmetric_tree(sol):
    # Tree with only left child should have only right child after inversion
    root = build_tree_from_list([1, 2, None])
    inverted = sol.invertTree(root)
    assert tree_to_list(inverted) == [1, None, 2]