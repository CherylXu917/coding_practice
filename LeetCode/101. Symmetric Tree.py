# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue = [root.left, root.right]
        while queue:
            left_root, right_root = queue.pop(0), queue.pop(0)
            if left_root is None and right_root is None:
                continue
            if left_root is None and right_root is not None:
                return False
            if left_root is not None and right_root is None:
                return False
            if left_root.val != right_root.val:
                return False
            queue.append(left_root.left)
            queue.append(right_root.right)
            queue.append(left_root.right)
            queue.append(right_root.left)
        return True


# recursive
class Solution2:
    def is_mirror(self, left_root, right_root):
        if left_root is None and right_root is None:
            return True
        if left_root is None and right_root is not None:
            return False
        if left_root is not None and right_root is None:
            return False
        if left_root.val != right_root.val:
            return False
        is_mirror1 = self.is_mirror(left_root.left, right_root.right)
        is_mirror2 = self.is_mirror(left_root.right, right_root.left)
        return is_mirror1 and is_mirror2

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)

#     # original
class Solution3:
    def is_symmetric_arr(self, arr):
        i, j = 0, len(arr)-1
        while i<j:
            if arr[i] and arr[j] and arr[i].val != arr[j].val:
                return False
            if (arr[i] == None and arr[j] != None) or (arr[j] == None and arr[i] != None):
                return False

            i += 1
            j -= 1
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        arr = [root]
        while arr:
            if self.is_symmetric_arr(arr):
                new_arr = []
                for i in range(len(arr)):
                    if arr[i] is not None:
                        new_arr.append(arr[i].left)
                        new_arr.append(arr[i].right)
                arr = new_arr
            else:
                return False
        return True



