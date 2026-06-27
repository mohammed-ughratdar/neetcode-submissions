class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict()

        for n in nums:
            if n in mydict:
                mydict[n] += 1
            else:
                mydict[n] = 1

        sorted_dict = sorted(mydict, key=lambda x:mydict[x], reverse=True)

        return sorted_dict[:k]