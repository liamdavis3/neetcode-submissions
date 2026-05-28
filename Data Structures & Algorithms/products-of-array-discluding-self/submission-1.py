import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        mult = {}
        for i, num in enumerate(nums):
            mult[i] = nums[:i] + nums[i+1:]

        for key in mult:
            answer.append(math.prod(mult[key]))
        return answer

