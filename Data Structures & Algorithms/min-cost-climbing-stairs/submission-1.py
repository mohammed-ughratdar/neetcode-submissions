class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        bottom_up = [0] * (len(cost) + 1)
        bottom_up[-1] = 0
        bottom_up[-2] = cost[-1]

        for x in range(len(cost)-2, -1, -1):
            bottom_up[x] = cost[x] + min(bottom_up[x+1], bottom_up[x+2])

        return min(bottom_up[0], bottom_up[1])