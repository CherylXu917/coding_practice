# http://prochal.com/2019/06/the-jungle-book/

from collections import deque

class Node:
    def __init__(self):
        self.children = []


def dfs(u, arr_node):
    ret = 0
    for child in arr_node[u].children:
        ret = max(ret, dfs(child, arr_node) + 1)
    print("Debug -- Node %d Height %d" % (u, ret))
    return ret


def set_up_tree(arr):
    arr_node = [Node() for _ in arr]

    roots = []
    for child, parent in enumerate(arr):
        if parent == -1:
            roots.append(child)
        else:
            arr_node[parent].children.append(child)

    ans = 0
    for root in roots:
        ans = max(ans, dfs(root, arr_node) + 1)

    return ans


if __name__ == '__main__':
    height = set_up_tree([-1, 8, 6, 0, 7, 3, 8, 9, -1, 6, 1])
    print(height)
