class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0,0
        minimum_size = 1000000
        current_sum = nums[left]


        while left < len(nums):
            if current_sum>=target:
                print(f"Left: {nums[left]} Right:{nums[right]}")
                minimum_size= min(minimum_size,right-left+1)
                current_sum-=nums[left]
                left+=1

            elif right+1<len(nums):
                right+=1
                current_sum+=nums[right]
            
            else: 
                current_sum-=nums[left]
                left+=1
                
        return 0 if minimum_size == 1000000 else minimum_size

