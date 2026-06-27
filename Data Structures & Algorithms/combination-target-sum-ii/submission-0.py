class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def dfs(i, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return

            if i >= len(candidates) or total > target:
                return

            curr_list.append(candidates[i])
            dfs(i+1, curr_list, total + candidates[i])
            curr_list.remove(candidates[i])
            
            while(i < len(candidates)-1 and candidates[i+1] == candidates[i]):
                i+=1
            dfs(i+1, curr_list, total)

        
        dfs(0, [], 0)

        return res