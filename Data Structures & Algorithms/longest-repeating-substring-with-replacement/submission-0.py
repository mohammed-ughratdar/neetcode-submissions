class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = dict()
        max_val_in_dict = 0
        l,r = 0, 0
        res = 0

        while r < len(s):
            my_dict[s[r]] = my_dict.get(s[r], 0)+1
            max_val_in_dict = max(max_val_in_dict, my_dict[s[r]])
            if (r-l+1) - max_val_in_dict <= k:
                res = max(res, r-l+1)
            else:
                my_dict[s[l]] -= 1
                l+=1
            r+=1

            
        return res

            
