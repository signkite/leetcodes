class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str = new_str + c

        rev_str = new_str[::-1]
        if rev_str == new_str:
            return True
        else:
            return False
