class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        crrnt_sum = 0

        for i in range(len(nums)):
            if crrnt_sum <0:
                crrnt_sum =0
            crrnt_sum +=nums[i]
            max_sum = max(crrnt_sum, max_sum)

        return max_sum