class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        dict_s, dict_t = {},{}

        for x in t:
            dict_t[x] = dict_t.get(x,0)+1

        haves, needs = 0, len(dict_t)

        res_itrs = [-1, -1]
        min_res_length = float("infinity")
        l=0

        for r in range(len(s)):

            dict_s[s[r]] = dict_s.get(s[r],0)+1

            if s[r] in dict_t and dict_s[s[r]] == dict_t[s[r]]:
                haves+=1

            while haves == needs:
                if (r-l+1) < min_res_length:
                    res_itrs = [l,r]
                    min_res_length = r-l+1


                dict_s[s[l]] -=1
                if s[l] in dict_t and dict_s[s[l]] < dict_t[s[l]]:
                    haves-=1
                l+=1

        a,b = res_itrs
        return s[a:b+1] if min_res_length != float("infinity") else ""
