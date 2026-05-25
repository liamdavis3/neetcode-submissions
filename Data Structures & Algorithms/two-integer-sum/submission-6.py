class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        totals = {}

        for i, num in enumerate(nums):
            if target-num in totals and totals[target-num] != i:
                answer = [totals[target-num], i]
                return sorted(answer)
            totals[num] = i

            