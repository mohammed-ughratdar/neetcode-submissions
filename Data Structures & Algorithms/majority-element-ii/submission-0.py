class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_map = {}
        res_list = []

        min_for_majority = len(nums)//3

        for num in nums:
            count_map[num] = count_map.get(num,0)+1

        for k,v in count_map.items():
            if v > min_for_majority:
                res_list.append(k)

        return res_list