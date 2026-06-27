class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 1
        max_sum = nums[0]
        sum_uptil_now = max_sum

        while r < len(nums):
            sum_uptil_now = max(nums[r], sum_uptil_now + nums[r])
            max_sum = max(max_sum, sum_uptil_now)
            r+=1

        return max_sum

            