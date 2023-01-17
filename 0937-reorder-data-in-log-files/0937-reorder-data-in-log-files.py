class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # (identifier, content) 로 나누고
        # content 순으로 정렬한다음
        # identifier 순으로 정렬
        letter_log_list = []
        digit_log_list = []
        for log in logs:
            if log.split()[1].isdigit():
                digit_log_list.append(log)
            else:
                letter_log_list.append((log.split()[0], " ".join(log.split()[1:])))
        
        letter_log_list.sort(key=lambda x: (x[1], x[0]))
        letter_log_list = list(map(lambda x: x[0] + ' ' + x[1], letter_log_list))
        return letter_log_list + digit_log_list