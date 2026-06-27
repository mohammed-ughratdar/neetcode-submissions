class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map_of_distances = dict()
        res = []

        for pt in points:
            distance_from_origin = math.sqrt(pt[0]*pt[0] + pt[1]*pt[1])
            map_of_distances.setdefault(distance_from_origin, []).append(pt)

        keys = []
        for key,v in map_of_distances.items():
            keys.append(key)
            

        heapq.heapify(keys)

        while k>0:
            pt = map_of_distances[heapq.heappop(keys)]
            len_of_pt = len(pt)
            res.extend(pt)
            k -= len_of_pt

        return res