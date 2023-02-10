class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        match = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        answer = [*match[digits[0]]]
        for num in digits[1:]:
            case = [*match[num]]
            temp = answer.copy()
            answer.clear()
            for alp_str in temp:
                for c in case:
                    answer.append(alp_str + c)
            
        return answer
        
        
    