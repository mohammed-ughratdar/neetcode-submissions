class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for x in nums:
            if my_dict.get(x) == None:
                my_dict[x] = 1
            else:
                return True
            
        return False