def is_pal(s):
    if s == s[::-1]:
        return True
    else:
        return False


class Solution:
    def longestPalindrome(self, s: str) -> str:
        check_len = len(s)
        while check_len:
            for start in range(len(s) - check_len + 1):
                end = start + check_len
                if is_pal(s[start:end]):
                    return s[start:end]
            check_len -= 1
