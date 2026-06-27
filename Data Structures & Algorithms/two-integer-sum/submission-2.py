class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for x in range(0, len(nums)):
            if (target - nums[x]) in myMap:
                return sorted([x, myMap[target-nums[x]]])
            myMap[nums[x]] = x

        return []   

