class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        
        former = prices[0]
        cur_min = 10001
        for price in prices:
            # 가격의 오름세가 있다면
            if price > former:
                
                # 최저점에 변동이 있다면 최저점 갱신
                if cur_min > former:
                    cur_min = former
                
                # 최고 이윤 후보군에 (오른 가격 - 현재까지의 최저점) 추가
                profit.append(price - cur_min)
            
            former = price
        return max(profit)
            
        