class Solution:
    def rob(self, nums: List[int]) -> int:
        i_minus_one_max = 0
        i_minus_two_max = 0

        for n in nums:
            temp = max(n + i_minus_two_max, i_minus_one_max)
            i_minus_two_max = i_minus_one_max
            i_minus_one_max = temp

        return i_minus_one_max