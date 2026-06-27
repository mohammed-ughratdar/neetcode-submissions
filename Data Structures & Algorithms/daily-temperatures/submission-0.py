class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices_stack = []
        final_list = [0]*len(temperatures)

        for x in range(0, len(temperatures)):
            top = indices_stack[-1] if len(indices_stack)>0 else None

            if top != None and temperatures[x] > temperatures[top]:
                while(len(indices_stack)>0 and temperatures[x] > temperatures[top]):
                    final_list[top] = x-top
                    indices_stack.pop()
                    top = indices_stack[-1] if len(indices_stack)>0 else None
                
            indices_stack.append(x)
        
        return final_list
