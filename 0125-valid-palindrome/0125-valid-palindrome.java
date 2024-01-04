import java.io.*;

class Solution {
    public boolean isPalindrome(String s) {
        String str = "";
        char c;
        // s 내부 숫자 및 영어가 아닌 문자는 필터링, 영어 대문자는 소문자로 변환
        for (int i = 0; i < s.length(); ++i) {
            c = s.charAt(i);
            if ('A' <= c && c <= 'Z') {
                c = (char)(c - 'A' + 'a');
                str += c;
            } else if ('a' <= c && c <='z' || '0' <= c && c <= '9') {
                str += c;
            }
        }
        
        // 변환된 문자열의 palindrome 여부 확인
        boolean is_pal = true;
        for (int i = 0; i < str.length(); ++i) {
            if (str.charAt(i) != str.charAt(str.length() - 1 - i)) {
                is_pal = false;
                break;
            }
        }
        
        return is_pal;
    }
}