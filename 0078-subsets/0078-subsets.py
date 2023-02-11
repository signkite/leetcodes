class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        
        def dfs(left_nums, cur_set, count):
            if count == 1:
                for num in left_nums:
                    answer.append(cur_set + [num])
            
            for i in range(len(left_nums) - 1):
                dfs(left_nums[i + 1:], cur_set + [left_nums[i]], count - 1)
        
        for cnt in range(1, len(nums) + 1):
            dfs(nums, [], cnt)
        
        return answer
        