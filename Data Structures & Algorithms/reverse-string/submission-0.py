class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        temp_s = ''
        x,y = 0, len(s)-1

        while x<y:
            temp_s = s[x]
            s[x] = s[y]
            s[y] = temp_s

            x+=1
            y-=1
            
        
        