class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated_stones = [-s for s in stones]
        heapq.heapify(negated_stones)

        while len(negated_stones) > 1:
            first_stone = heapq.heappop(negated_stones)
            second_stone = heapq.heappop(negated_stones)

            if first_stone != second_stone:
                heapq.heappush(negated_stones, -1*abs(first_stone-second_stone))

        return -negated_stones[0] if negated_stones else  0