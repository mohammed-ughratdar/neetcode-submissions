class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_so_far, r, max_so_far = 0, 1, 0

        while(r != len(prices)):
            if prices[r]-prices[lowest_so_far] >= max_so_far:
                max_so_far = prices[r]-prices[lowest_so_far]

            if prices[r] < prices[lowest_so_far]:
                lowest_so_far = r
            
            r+=1

        return max_so_far
