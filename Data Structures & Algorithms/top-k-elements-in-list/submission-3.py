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

        for num,freq in freq_elements.items():
            buckets[freq].append(num)
        
        for count in range(len(buckets) - 1, 0, -1): 
            if len(buckets[count]) != 0:
                for n in buckets[count]:
                    final_list.append(n)

        return  final_list[:k]
            
        
        
