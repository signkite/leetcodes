class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def c(left_num, cur_nums, count):
            if count == 1:
                for num in left_num:
                    answer.append(cur_nums + [num])
            
            for i, num in enumerate(left_num):
                if i == len(left_num) - 1:
                    break
                    
                new_left_num = left_num[i + 1:]
                
                new_cur_nums = cur_nums.copy()
                new_cur_nums.append(num)
                
                c(new_left_num, new_cur_nums, count - 1)
                
        num_list = list(range(1, n + 1))
        answer = []
        c(num_list, [], k)
        return answer