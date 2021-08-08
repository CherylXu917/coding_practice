class Solution:
    def permute(self, nums):
        res = [[]]
        for i, n in enumerate(nums):
            new_res = []
            for j in range(len(res)):
                res[j].append(n)  # append to the end
                for k in range(i):
                    new_res.append(res[j][:k] + [n] + res[j][k:-1])
            res = res + new_res
        return res

