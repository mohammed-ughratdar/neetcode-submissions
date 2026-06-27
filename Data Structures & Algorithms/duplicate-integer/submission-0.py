class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict_counter = {}

        for x in nums:
            if x in dict_counter:
                return True
            
            dict_counter[x] = 1

        return False