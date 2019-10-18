class Solution:
    def find_combination(self, candidates, target, i, cur_com, res):

        if target == 0:
            res.append(cur_com)
            return None
        if i >= len(candidates):
            return None
        cur_sum = 0
        n_candidates = []
        while cur_sum <= target:
            # backtracking
            self.find_combination(candidates, target - cur_sum, i + 1, cur_com + n_candidates, res)
            n_candidates.append(candidates[i])
            cur_sum += candidates[i]
        return None

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        res = []
        self.find_combination(candidates, target, 0, [], res)
        return res

    # solution 2: very neat
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = [(0, target, [])]
        while stack:
            i, t, res = stack.pop()
            for k, j in enumerate(candidates[i:], i):
                if j < t:
                    stack.append((k, t - j, res + [j]))
                elif j == t:
                    ans.append(res + [t])
        return ans

