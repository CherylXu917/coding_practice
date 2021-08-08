import math
# Add any extra import statements you may need here
from collections import deque

class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here
def reverse_end(pre, cur, rev_start, rev_pre):
  rev_start.next = cur
  rev_pre.next = pre


def reverse(head):
    # Write your code here
    pre = root = Node(-1)
    cur = root.next = head
    is_reverse = False
    while cur:
        if not is_reverse:
            if cur.data % 2 == 0:
                is_reverse = True
                rev_pre, rev_start = pre, cur
        else:
            if cur.data % 2 == 0:
                cur.next, pre, cur = pre, cur, cur.next
                continue
            else:
                is_reverse = False
                reverse_end(pre, cur, rev_start, rev_pre)
        pre, cur = cur, cur.next

    if is_reverse:
        reverse_end(pre, cur, rev_start, rev_pre)
    return root.next


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        n = len(s)
        cur = pre = start = 0
        end = 0
        total = len(t_map)
        min_len = n + 1

        while cur < n:
            while total and cur < n:
                if s[cur] not in t_map:
                    cur += 1
                    continue
                t_map[s[cur]] -= 1
                if t_map[s[cur]] == 0:
                    total -= 1
                cur += 1

            if total != 0:
                break

            while total == 0 and pre <= cur:
                if s[pre] in t_map:
                    pre += 1
                    continue

                if t_map[s[pre]] == 0:
                    total += 1
                t_map[s[pre]] += 1
                pre += 1

            if cur - pre + 1 < min_len:
                min_len = cur - pre + 1
                start = pre - 1
                end = cur

        return s[start: end]