class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        paragraph = paragraph.replaceAll("[^A-Za-z0-9]+", " ").toLowerCase();
        List<String> ban_list = Arrays.asList(banned);
        Map<String, Integer> counter = new HashMap<>();
        for(String word: paragraph.split(" ")) {
            if (!ban_list.contains(word))
                counter.put(word, counter.getOrDefault(word, 0) + 1);
        }
        
        int max_count = 0;
        String answer = "";
        for (Map.Entry<String, Integer> entry: counter.entrySet()) {
            Integer value = entry.getValue();
            if (max_count < value) {
                answer = entry.getKey();
                max_count = entry.getValue();
            }
        }
        
        return answer;
    }
}