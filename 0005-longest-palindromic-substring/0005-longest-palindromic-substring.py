def is_pal(s):
    i = 0
    while i < len(s) // 2:
        if s[i] != s[-1 - i]:
            return False
        i += 1
    return True


class Solution:
    def longestPalindrome(self, s: str) -> str:
        check_len = len(s)
        while check_len:
            for start in range(len(s) - check_len + 1):
                end = start + check_len
                if is_pal(s[start:end]):
                    return s[start:end]
            check_len -= 1
