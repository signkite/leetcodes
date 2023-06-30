class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        
        i = 0
        while True:
            if len(strs[0]) == i:
                return answer
            
            c = strs[0][i]
            for s in strs:
                if len(s) == i or s[i] != c:
                    return answer
            
            answer += c
            i += 1
            