class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count_dict = {}
        s_counter = 0

        for x in s:
            if x in count_dict:
                count_dict[x] += 1
            else:
                count_dict[x] = 1
            s_counter += 1
                
        
        for y in t:
            if y in count_dict and count_dict[y] > 0:
                count_dict[y] -= 1
                s_counter -= 1

            else:
                return False

        return s_counter == 0