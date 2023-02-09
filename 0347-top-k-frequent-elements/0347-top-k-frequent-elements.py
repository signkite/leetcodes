class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        output = []
        for num, _ in counter.most_common(k):
            output.append(num)
            
        return output