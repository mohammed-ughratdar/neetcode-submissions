class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr_1 = ptr_2 = 0
        res = ""

        while ptr_1 <len(word1) and ptr_2 <len(word2):
            res +=  "".join(word1[ptr_1])
            res += "".join(word2[ptr_2])
            ptr_1+=1
            ptr_2+=1

        while ptr_1 <len(word1):
            res += "".join(word1[ptr_1])
            ptr_1+=1
            
        while ptr_2 <len(word2):
            res += "".join(word2[ptr_2])
            ptr_2+=1

        return res