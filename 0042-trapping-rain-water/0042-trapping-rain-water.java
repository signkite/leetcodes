class Solution {
    public int trap(int[] height) {
        int answer = 0;
        
        // 최대 값이 존재하는 index를 찾는다.
        int maxIdx = 0;
        int maxHeight = -1;
        for(int i = 0, size = height.length; i < size; ++i) {
            if (height[i] > maxHeight) {
                maxHeight = height[i];
                maxIdx = i;
            }
        }
        
        // 처음 ~ 첫 번째 최대 높이 기둥이 존재하는 곳 까지 빗물의 양
        int curMaxHeight = 0;
        int sum = 0;
        for (int i = 0; i <= maxIdx; ++i) {
            // 이전 최대 높이 이상의 기둥을 만난다면
            if (curMaxHeight < height[i]) {
                curMaxHeight = height[i];
                answer += sum;
                sum = 0;
            } else {
                sum += curMaxHeight - height[i];
            }
        }
        
        // 첫 번째 최대 높이 기둥 ~ 끝까지의 빗물의 양
        // 뒤에서부터 거꾸로 오며 위의 로직을 반복한다.
        curMaxHeight = 0;
        for (int i = height.length - 1; i >= maxIdx; --i) {
            if (curMaxHeight <= height[i]) {
                curMaxHeight = height[i];
                answer += sum;
                sum = 0;
            } else {
                sum += curMaxHeight - height[i];
            }
        }
        
        return answer;
    }
}