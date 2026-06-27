class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_list = [[]]

        for num in nums:
            size = len(final_list)
            for y in range(0, size):
                subset_list = final_list[y].copy()
                subset_list.append(num)
                final_list.append(subset_list)

        return final_list
