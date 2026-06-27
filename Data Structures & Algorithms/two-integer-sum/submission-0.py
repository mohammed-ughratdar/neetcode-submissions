class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumsList = []
        lenOfList = len(nums)

        for x in range(0, lenOfList):
            for y in range(x+1, lenOfList):
                if nums[x]+nums[y] == target:
                    twoSumsList.append(x)
                    twoSumsList.append(y)
        
        return twoSumsList
