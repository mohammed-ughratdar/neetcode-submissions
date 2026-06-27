class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        for x in range(0, len(strs[0])):
            for y in strs:
                if x == len(y) or y[x] != strs[0][x]:
                    return result
                
            result+= strs[0][x]
        
        return result
