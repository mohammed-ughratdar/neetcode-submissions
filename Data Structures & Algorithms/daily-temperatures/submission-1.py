class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices_stack = []
        final_list = [0]*len(temperatures)

        for x in range(0, len(temperatures)):
            

            if indices_stack and temperatures[x] > temperatures[indices_stack[-1]]:
                while(indices_stack and temperatures[x] > temperatures[indices_stack[-1]]):
                    final_list[indices_stack[-1]] = x-indices_stack[-1]
                    indices_stack.pop()
                
            indices_stack.append(x)
        
        return final_list
