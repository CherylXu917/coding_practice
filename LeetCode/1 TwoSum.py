class Solution:
    def twoSum(self, nums, target: int):
        sum_dict = {}
        for i, n in enumerate(nums):
            m = target - n  # number to find
            if m not in sum_dict:
                sum_dict[n] = i
            else:
                return [sum_dict[m], i]




