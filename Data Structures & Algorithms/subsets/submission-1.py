class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        subset_list = []

        def dfs(nums, final_list, subset_list, i):

            if len(nums) == i:
                final_list.append(subset_list.copy())
                return

            subset_list.append(nums[i])

            dfs(nums, final_list, subset_list, i+1)
            subset_list.pop()
            dfs(nums,final_list, subset_list, i+1)

            return final_list

        return dfs(nums, final_list, subset_list, 0)

