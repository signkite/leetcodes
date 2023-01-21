class Solution:
    def trap(self, height: List[int]) -> int:
        # 앞에서부터 최고점, 현재 지점 높이를 가지고 가다가
        # 현재의 최고점과 같거나 보다 높은 기둥을 만나면 아래 두가지를 수행
        # 1. 최고점 갱신
        # 2. 현재까지 저장된 물 높이를 총 물 량에 갱신
        whole_water = 0
        cur_water = 0
        peak = 0
        
        for h in height:
            if h >= peak:
                peak = h
                whole_water += cur_water
                cur_water = 0
            else:
                cur_water += peak - h
        
        # 최고점이 나온 후 끝까지는 계산되지 않는다.
        # 따라서 최고점이 나올 때까지 거꾸로 한 번 수행
        cur_water = 0
        end = peak
        peak = 0
        
        height.reverse()
        for h in height:
            if h == end:
                whole_water += cur_water
                break
                
            if h >= peak:
                peak = h
                whole_water += cur_water
                cur_water = 0
            else:
                cur_water += peak - h
        
        return whole_water