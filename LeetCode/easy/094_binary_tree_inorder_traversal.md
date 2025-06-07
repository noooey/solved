# 094. Binary Tree Inorder Traversal

## Code (Python)
```python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            answer.append(current.val)
            current = current.right
```

## Complexity
- Time: O(n)

## Notes
- Stack
