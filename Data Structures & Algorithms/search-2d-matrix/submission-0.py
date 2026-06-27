class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        
        

        while(l<=r):
            mid = (l+r)//2

            if matrix[mid][-1] < target:
                l= mid+1
                
            elif matrix[mid][0] > target:
                r = mid-1

            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                internal_l, internal_r = 0, len(matrix[mid])-1

                while(internal_l<=internal_r):
                    arr_mid = (internal_l+internal_r)//2

                    if matrix[mid][arr_mid] == target:
                        return True

                    if matrix[mid][arr_mid] < target:
                        internal_l = arr_mid+1

                    elif matrix[mid][arr_mid] > target:
                        internal_r = arr_mid-1
                        
                return False

        return False

                    
                    
            
            




            