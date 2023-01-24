class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        prev = 100001
        
        # '정렬 후' 투포인터 방식으로 접근
        # 미리 정렬되어있으므로 오른쪽 포인터에서 왼쪽으로 당기면 적은 수를 선택하게 됨
        # 반대로 왼쪽 포인터를 오른쪽으로 밀면 큰 수를 선택하게 됨
        # 같은 수의 조합이 결과에 포함되면 안되므로 같은 조합은 피하는 알고리즘을 적용해야함.
        for i in range(len(nums) - 2):
            if prev == nums[i]:
                continue
            else:
                prev = nums[i]
            
            left_ptr = i + 1
            right_ptr = len(nums) - 1
            
            while left_ptr < right_ptr:
                if nums[i] + nums[left_ptr] + nums[right_ptr] > 0:
                    right_ptr -= 1
                elif nums[i] + nums[left_ptr] + nums[right_ptr] < 0:
                    left_ptr += 1
                else:
                    answer.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    while left_ptr < right_ptr and nums[left_ptr + 1] == nums[left_ptr]:
                        left_ptr += 1
                    while left_ptr < right_ptr and nums[right_ptr - 1] == nums[right_ptr]:
                        right_ptr -= 1
                    
                    left_ptr += 1
                    right_ptr -= 1
                    
        return answer