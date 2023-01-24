class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 왼쪽으로부터 곱해온 결과 저장
        left_stack = [nums[0]]
        
        # 오른쪽으로부터 곱해온 결과 저장
        right_stack = [nums[-1]] * len(nums)
        
        for i in range(1, len(nums)):
            left_stack.append(left_stack[i - 1] * nums[i])
            right_stack[-i - 1] = right_stack[-i] * nums[-i - 1]
        
        # answer[i]는 left_stack[i - 1] * right_stack[i + 1]
        answer = [right_stack[1]]
        for i in range(1, len(nums) - 1):
            answer.append(left_stack[i - 1] * right_stack[i + 1])
        answer.append(left_stack[-2])
        return answer