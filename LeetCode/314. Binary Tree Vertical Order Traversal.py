"""
314. Binary Tree Vertical Order Traversal
Medium

1615

212

Add to List

Share
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Example 4:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

# solution 1
from collections import deque, defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        que = deque([(root, 0)])
        col_map = defaultdict(list)
        while que:
            node, x = que.popleft()
            if not node:
                continue
            col_map[x].append(node.val)
            que.append((node.left, x - 1))
            que.append((node.right, x + 1))
        res = []
        for col in sorted(col_map):
            res.append(col_map[col])
        return res

# solution 2
from collections import deque, defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque([(root, 0)])
        res = defaultdict(list)
        lt = rt = 0
        while que:
            node, x = que.popleft()
            res[x].append(node.val)
            if node.left:
                que.append((node.left, x - 1))
                lt = min(lt, x - 1)
            if node.right:
                que.append((node.right, x + 1))
                rt = max(rt, x + 1)
        out = []
        for x in range(lt, rt + 1):
            out.append(res[x])
        return out