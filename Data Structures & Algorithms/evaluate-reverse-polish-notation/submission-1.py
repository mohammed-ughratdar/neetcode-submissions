class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        char_tokens = ['+', '-', '/', '*']

        def ops(num1, num2, operator):
            if operator == '+':
                return num2 + num1
            if operator == '-':
                return num2 - num1 
            if operator == '/':
                return int(num2 / num1)  
            if operator == '*':
                return num2 * num1

        for x in tokens:
            if x not in char_tokens:
                my_stack.append(int(x))
            elif x == '+':
                if len(my_stack) >=2:
                    my_stack.append(ops(my_stack.pop(), my_stack.pop(), '+'))
            elif x == '-':
                if len(my_stack) >=2:
                    my_stack.append(ops(my_stack.pop(), my_stack.pop(), '-'))
            elif x == '/':
                if len(my_stack) >=2:
                    my_stack.append(ops(my_stack.pop(), my_stack.pop(), '/'))
            elif x == '*':
                if len(my_stack) >=2:
                    my_stack.append(ops(my_stack.pop(), my_stack.pop(), '*'))
        return my_stack.pop()

