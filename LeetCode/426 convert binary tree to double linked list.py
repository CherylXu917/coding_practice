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


