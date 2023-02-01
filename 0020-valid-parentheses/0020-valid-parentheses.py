class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter in '({[':
                stack.append(letter)
            elif letter == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif letter == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif letter == ']':
                if not stack or stack.pop() != '[':
                    return False
        
        if stack:
            return False
        else:
            return True
            
                
            