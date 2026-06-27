class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_stack = []
        graph_pts = list(zip(position,speed))
        graph_pts = sorted(graph_pts, key= lambda p: p[0], reverse=True)

        for pt in graph_pts:
            time_to_target = (target-pt[0])/pt[1]
            if fleet_stack and fleet_stack[-1] >= time_to_target:
                continue
            else:
                fleet_stack.append(time_to_target)

        return len(fleet_stack)
