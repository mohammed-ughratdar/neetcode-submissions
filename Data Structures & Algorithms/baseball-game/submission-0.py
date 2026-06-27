class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = []
        result = 0
            

        for op in operations:
            if op == "+":
                if len(my_stack) >= 2:
                    my_stack.append(my_stack[-1]+my_stack[-2])

            elif op == "C":
                if len(my_stack) > 0:
                    my_stack.pop()

            elif op == "D":
                if my_stack:
                    my_stack.append(my_stack[-1]*2)

            else:
                my_stack.append(int(op))

        while my_stack:
            result+= my_stack.pop()

        return result

            

