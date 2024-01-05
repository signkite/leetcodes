class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letterLogs = new ArrayList<>();
        List<String> digitLogs = new ArrayList<>();
        
        for (String log: logs) {
            // log 부분의 첫 번째 문자에 따라 로그 종류를 구분
            if (Character.isDigit(log.split(" ", 2)[1].charAt(0))) {
                digitLogs.add(log);
            } else {
                letterLogs.add(log);
            }
        }
        
        letterLogs.sort((s1, s2) -> {
            String[] s1Arr = s1.split(" ", 2);
            String[] s2Arr = s2.split(" ", 2);
            
            int cmp = s1Arr[1].compareTo(s2Arr[1]);
            if (cmp == 0) {
                return s1Arr[0].compareTo(s2Arr[0]);
            } else {
                return cmp;
            }
        });
        
        letterLogs.addAll(digitLogs);
        String[] answer = letterLogs.toArray(new String[letterLogs.size()]);
    
        return answer;
    }
}