class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        l,r = 1, piles[-1]
        global_count = r
        while(l<r):
            total_hours = 0
            all_counted_flag = True
            nr_of_bananas_to_eat = (l+r)//2
            for x in piles:
                hours_taken = math.ceil(x/nr_of_bananas_to_eat)
                total_hours += hours_taken
                if total_hours > h:
                    all_counted_flag = False
                    break
                
            if all_counted_flag:
                global_count = min(global_count, nr_of_bananas_to_eat)
                r = nr_of_bananas_to_eat
            else:
                l = nr_of_bananas_to_eat+1

        return global_count    
                

