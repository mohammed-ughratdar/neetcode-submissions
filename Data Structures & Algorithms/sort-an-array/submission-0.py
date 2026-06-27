class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, R, M):
            left_sector = arr[L: M+1]
            right_sector = arr[M+1: R+1]
            i, j, k = L, 0, 0

            while j < len(left_sector) and k < len(right_sector):
                if left_sector[j] <= right_sector[k]:
                    arr[i] = left_sector[j]
                    j += 1
                
                else:
                    arr[i] = right_sector[k]
                    k += 1
                i += 1

            while j < len(left_sector):
                arr[i] = left_sector[j]
                j += 1
                i += 1
            
            while k < len(right_sector):
                arr[i] = right_sector[k]
                k += 1
                i += 1



        def mergeSort(nums, l, r):
            if l==r:
                return nums

            mid = (l+r)//2
            mergeSort(nums, l, mid)
            mergeSort(nums, mid+1, r)

            merge(nums, l, r, mid)

            return nums

        return mergeSort(nums, 0, len(nums))