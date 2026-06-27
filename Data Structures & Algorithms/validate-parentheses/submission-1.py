class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for x in range(0, len(s)):
            if s[x] in ['(','[','{']:
                my_stack.append(s[x])
            elif s[x] in [')',']','}']:
                if len(my_stack) is 0:
                    return False
                if s[x] == '}' and my_stack[-1] == '{':
                    my_stack.pop()
                elif s[x] == ')' and my_stack[-1] == '(':
                    my_stack.pop()
                elif s[x] == ']' and my_stack[-1] == '[':
                    my_stack.pop() 
                else:
                    return False

        if len(my_stack) != 0:
            return False
        return True