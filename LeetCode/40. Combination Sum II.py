class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        stack = [(0, target, [])]
        while stack:
            i, cur_sum, combination = stack.pop()
            for j, candidate in enumerate(candidates[i:], i):
                if j > i and candidate == candidates[j - 1]:
                    continue
                if candidate == cur_sum:
                    res.append(combination + [candidate])
                elif candidate < cur_sum:
                    stack.append([j + 1, cur_sum - candidate, combination + [candidate]])
        return res


