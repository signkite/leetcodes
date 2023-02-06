class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_cnt = len(stones)
        
        for jewel in jewels:
            stones = stones.replace(jewel, "")
        
        return stone_cnt - len(stones)