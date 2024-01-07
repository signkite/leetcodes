class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answer = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        
        // 문자열 정렬
        // hashMap에 있는지 판단
        // 없다면 ArrayList 추가
        // 있다면 문자 추가
        for (String str: strs) {
            List<Character> cList = new ArrayList<>();
            for (char c: str.toCharArray()) {
                cList.add(c);
            }
            cList.sort((c1, c2) -> c1 - c2);
            StringBuilder sb = new StringBuilder();
            
            for (char c: cList) {
                sb.append(c);    
            }
            
            String orderedStr = sb.toString();
            if (map.containsKey(orderedStr)) {
                map.get(orderedStr).add(str);
            } else {
                List<String> newList = new ArrayList<>();
                newList.add(str);
                map.put(orderedStr, newList);
            }
        }
        
        for (Map.Entry<String, List<String>> entry: map.entrySet()) {
            answer.add(entry.getValue());
        }
        
        return answer;
    }
}