class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, mid = 0, len(nums)-1, len(nums)//2

        while(l <= r):

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                l = mid+1

            elif target < nums[mid]:
                r = mid-1
            
            mid = (r+l)//2

        return -1
            