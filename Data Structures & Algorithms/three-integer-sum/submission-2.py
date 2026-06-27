class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final_list = list()
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1
            
            while j<k:
                three_sum = nums[i]+nums[j]+nums[k]
                if three_sum > 0:
                    k -= 1

                elif three_sum < 0:
                    j += 1

                else:
                    final_list.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while(nums[j]==nums[j-1] and j<k):
                        j+=1
                    while(nums[k]==nums[k+1] and j<k):
                        k-=1 
                    
                

        return final_list

