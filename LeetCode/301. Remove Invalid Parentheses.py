class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def get_all_rmv_idx(wrong_idx, s, cmbn, res):
            """use recursion to get all wrong index combination"""
            if len(wrong_idx) == 0:
                res.append(cmbn)
                return
            if cmbn:
                pre = cmbn[-1]
            else:
                pre = -1
            rt = wrong_idx[0]
            for nxt in range(pre + 1, rt + 1):
                if s[nxt] != s[rt]:
                    continue
                # drop duplicate
                if nxt > pre + 1 and s[nxt] == s[nxt - 1]:
                    continue
                get_all_rmv_idx(wrong_idx[1:], s, cmbn + [nxt], res)

        # use stack to identify wrong position
        stack = []
        rt_rmv_idx = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
                continue
            if ch == ')':
                if stack:
                    stack.pop()
                    continue
                rt_rmv_idx.append(i)

        rt_rm_idx_cmb = []
        get_all_rmv_idx(rt_rmv_idx, s, [], rt_rm_idx_cmb)
        n = len(s)
        lt_rm_idx_cmb = []
        lt_rmv_idx = [n - 1 - i for i in reversed(stack)]
        get_all_rmv_idx(lt_rmv_idx, s[::-1], [], lt_rm_idx_cmb)
        lt_rm_idx_cmb = [[n - 1 - i for i in reversed(cmb)] for cmb in lt_rm_idx_cmb]
        rmv_idx = [set(rt + lt) for rt in rt_rm_idx_cmb for lt in lt_rm_idx_cmb]

        out = []
        for res in rmv_idx:
            new_st = ''
            for i in range(n):
                if i in res:
                    continue
                new_st += s[i]
            out.append(new_st)
        return out




