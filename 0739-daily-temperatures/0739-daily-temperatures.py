class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [(temperature, index), (), ... ]
        tem_stack = []
        answer = [0] * len(temperatures)
        
        for i, tem in enumerate(temperatures):
            while tem_stack and tem_stack[-1][0] < tem:
                tem_index = tem_stack.pop()[1]
                answer[tem_index] = i - tem_index
            
            tem_stack.append((tem, i))
                
        return answer
        
        