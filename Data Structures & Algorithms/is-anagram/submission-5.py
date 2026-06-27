class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sorted_a = sorted(s)
        sorted_b = sorted(t)

        for x in range(0, len(s)):
            if sorted_a[x] != sorted_b[x]:
                return False
        return True
        