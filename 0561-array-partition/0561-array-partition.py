class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 오름차순으로 정렬 후, nums[2n + 1]번째 수가 nums[2n]번째 수를 살려주면 최적의 경우
        nums.sort()
        return sum(nums[::2])