class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ptr_1 = ptr_2 = 0
        temp_res = []
        
        while ptr_1 < m and ptr_2 < n: 
            if nums1[ptr_1] > nums2[ptr_2]:
                temp_res.append(nums2[ptr_2])
                ptr_2+=1
            else:
                temp_res.append(nums1[ptr_1])
                ptr_1+=1

        while ptr_1 < m:
            temp_res.append(nums1[ptr_1])
            ptr_1+=1
        
        while ptr_2 < n:
            temp_res.append(nums2[ptr_2])
            ptr_2+=1

        for x in range(len(temp_res)):
            nums1[x] = temp_res[x]

        
        