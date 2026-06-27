class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elements = {}
        buckets = [[] for _ in range(0, len(nums)+1)]
        final_list = []

        for num in nums:
            if not num in freq_elements:
                freq_elements[num] = 1
            else:
                freq_elements[num] += 1

        for l,v in freq_elements.items():
            buckets[v].append(l)
        
        count = len(buckets)-1

        while(len(final_list) <= k):
            if len(buckets[count]) != 0:
                for n in buckets[count]:
                    final_list.append(n)
            count -= 1

        return  final_list[:k]
            
        
        
