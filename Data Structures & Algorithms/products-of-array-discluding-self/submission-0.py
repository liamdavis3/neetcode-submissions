class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    answer[i] *= num2

        return answer

