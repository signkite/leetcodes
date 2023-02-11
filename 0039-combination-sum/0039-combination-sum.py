class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(left_cand: List[int], cur_nums: List[int], cur_sum):
            if cur_sum > target:
                return
            elif cur_sum == target:
                answer.append(cur_nums.copy())
            else:
                for i, num in enumerate(left_cand):
                    new_left_cand = left_cand[i:]
                    new_cur_nums = cur_nums.copy()
                    new_cur_nums.append(num)
                    dfs(new_left_cand, new_cur_nums, cur_sum + num)
        
        dfs(candidates, [], 0)
        return answer