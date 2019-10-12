class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # runnning max ending in current position
        running_max = nums[0]
        sub_max = nums[0]
        for n in nums[1:]:
            running_max = n + max(0, running_max)
            sub_max = max(sub_max, running_max)
        return sub_max
