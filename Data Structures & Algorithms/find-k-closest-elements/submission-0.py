class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        my_list = []
        res = []

        for z in arr:
            heapq.heappush(my_list, (-abs(z-x), -z))
            if len(my_list) > k:
                heapq.heappop(my_list)

        for val in my_list:
            res.append(-1*val[1])

        return sorted(res)
        