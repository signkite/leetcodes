class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def permutation(left_num, cur_num):
            if len(left_num) == 1:
                answer.append(left_num + cur_num)
                return
            
            for n in left_num:
                new_left_num = left_num.copy()
                new_left_num.remove(n)
                
                new_cur_num = cur_num.copy()
                new_cur_num.append(n)
                permutation(new_left_num, new_cur_num)
            
        permutation(nums, [])
        return answer