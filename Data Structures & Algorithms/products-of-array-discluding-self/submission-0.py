class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_list, backward_list = [1 for _ in range(0, len(nums))],[1 for _ in range(0, len(nums))]


        for x in range(1, len(nums)):
            forward_list[x] = forward_list[x-1]*nums[x-1]

        for x in range(len(nums)-2, -1, -1):
            backward_list[x] = backward_list[x+1]*nums[x+1]

        return [forward_list[i]*backward_list[i] for i in range(0, len(nums))]