class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}
        for x in range(0, len(nums)):
            to_match = target - nums[x]
            if to_match in nums_dict:
                return [nums_dict.get(to_match), x]
            else:
                nums_dict[nums[x]] = x
        

