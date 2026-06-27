class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    # [3,4,5,6], target = 7
    # {3:0, 4:1, 5:2, 6:3}

    # [5,5], target = 10
    # {5:1}

        index_dict = {}

        for i,j in enumerate(nums):
            index_dict[j] = i

        for i, j in enumerate(nums):
            diff = target - j

            if diff in index_dict and index_dict[diff] != i:
                return [i, index_dict[diff]]