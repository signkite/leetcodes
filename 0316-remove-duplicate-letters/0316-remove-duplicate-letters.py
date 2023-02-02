class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        
        answer = []
        for c in s:
            # 앞에 자기보다 사전순으로 뒤인 알파벳이 있는데
            # 그 알파벳이 뒤에 또 나온다면 갈아치움
            
            if c not in answer:
                while answer and answer[-1] >= c and counter[answer[-1]] > 0:
                    answer.pop()
                answer += c
            
            counter[c] -= 1
        
        return "".join(answer)
        
        