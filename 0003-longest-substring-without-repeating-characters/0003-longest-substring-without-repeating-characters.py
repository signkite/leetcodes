class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_list = []
        max_len = 0
        
        for c in s:
            if c in cur_list:
                # 앞에 있는 문자가 나온 경우, 나왔던 문자를 포함한 앞쪽을 잘라내고
                # 최고 길이보다 길다면 최고 길이 갱신
                i = cur_list.index(c)
                length = len(cur_list)
                if length > max_len:
                    max_len = length
                
                if length > 1:
                    # 똑같은 문자가 연속해서 나오는 경우 index error 방지
                    cur_list = cur_list[i + 1:]
                    cur_list.append(c)
            else:
                cur_list.append(c)
        
        # 마지막으로 가능한 경우의 수가 max_len 보다 큰지 비교
        length = len(cur_list)
        if length > max_len:
            max_len = length
        
        return max_len
            
        
        