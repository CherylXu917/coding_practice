"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
Medium

1537

132

Add to List

Share
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.



Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# solution 1


class Solution:
    def __init__(self):
        self.tail = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        head = self.treeToDoublyList(root.left)

        if head:
            self.tail.right = root
            root.left = self.tail
        else:
            head = root

        self.tail = root
        root.right = self.treeToDoublyList(root.right)
        if root.right:
            root.right.left = root

        self.tail.right = head
        head.left = self.tail
        return head


# solution 2
class Solution:

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return None, None

            left_head, left_tail = dfs(root.left)
            right_head, right_tail = dfs(root.right)

            if left_head:
                head = left_head
                left_tail.right = root
                root.left = left_tail
            else:
                head = root

            if right_head:
                tail = right_tail
                root.right = right_head
                right_head.left = root
            else:
                tail = root
            return head, tail

        head, tail = dfs(root)

        if head:
            head.left = tail
            tail.right = head
        return head




"""
Previous Solution
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None

    def convertBinaryTree(self, root):
        if root is None:
            return None

        head = self.convertBinaryTree(root.left)

        if self.prev:
            root.left = self.prev
            self.prev.right = root
        else:
            head = root

        self.prev = root
        self.convertBinaryTree(root.right)

        return head

    def print_(self, head):
        while head:
            print(head.val)
            head = head.right


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(12)
    root.right = TreeNode(15)
    node = root.left
    node.left = TreeNode(25)
    node.right = TreeNode(30)
    node = root.right
    node.left = TreeNode(36)

    cls = Solution()
    head = cls.convertBinaryTree(root)
    cls.print_(head)


def aboveAverageSubarrays(arr):
    n = len(arr)
    sum_ = 0
    running_sum = [0] * n
    for i in range(n):
        sum_ += arr[i]
        running_sum[i] = sum_
    avg = sum_ / n
    res = []
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                cur_avg = running_sum[j] / (j + 1)
            else:
                cur_avg = (running_sum[j] - running_sum[i - 1]) / (j - i + 1)
            if cur_avg > avg:
                res.append([i + 1, j + 1])
    return res


