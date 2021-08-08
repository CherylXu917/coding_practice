class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LagestBST(root):

    def BSTUtil(root):

        if root is None:
            return True, 0, None, None

        is_lt_BST, lt_size, lt_min, lt_max = BSTUtil(root.left)
        is_rt_BST, rt_size, rt_min, rt_max = BSTUtil(root.right)

        if lt_min is None:
            lt_min = root.val
            lt_max = root.val - 1

        if rt_min is None:
            rt_max = root.val
            rt_min = root.val + 1

        if is_lt_BST and is_rt_BST:
            if lt_max < root.val < rt_min:
                return True, 1 + lt_size + rt_size, lt_min, rt_max

        return False, max(rt_size, lt_size), min(lt_min, rt_min), max(lt_max, rt_max)

    is_BST, size, min_, max_ = BSTUtil(root)
    return size


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    cur = root.left
    cur.left = Node(1)
    cur.right = Node(8)
    cur = root.right
    cur.right = Node(7)

    print(LagestBST(root))