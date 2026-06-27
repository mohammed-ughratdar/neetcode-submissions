class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = 1
        current_majority_element = nums[0]

        for x in range(1,len(nums)):
            if num_count <= 0 and nums[x] != current_majority_element:
                current_majority_element = nums[x]
                num_count+=1
            
            elif nums[x] == current_majority_element:
                num_count+=1

            elif nums[x] != current_majority_element:
                num_count-=1

        return current_majority_element