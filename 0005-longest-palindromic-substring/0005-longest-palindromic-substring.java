class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 1) return s;
        
        int maxLen = 0;
        String answer = "";
        
        // 길이가 홀수인 부분 회문 찾기
        int curLen = 0, i;
        for (int center = 0; center < s.length(); ++center) {
            i = 1;
            while (0 <= center - i && center + i < s.length()) {
                if (s.charAt(center - i) != s.charAt(center + i)) {
                    break;
                }
                i++;
            }
            curLen = 2 * (i - 1) + 1;
            if (curLen > maxLen) {
                maxLen = curLen;
                answer = s.substring(center - i + 1, center + i);
            }
        }
        
        // 길이가 짝수인 부분 회문 찾기
        for (int leftCenter = 0; leftCenter < s.length() - 1; ++leftCenter) {
            i = 0;
            while (0 <= leftCenter - i && leftCenter + i + 1 < s.length()) {
                if (s.charAt(leftCenter - i) != s.charAt(leftCenter + i + 1)) {
                    break;
                }
                i++;
            }
            curLen = 2 * i;
            if (curLen > maxLen) {
                maxLen = curLen;
                answer = s.substring(leftCenter - i + 1, leftCenter + i + 1);
            }
        }
        
        return answer;
    }
}