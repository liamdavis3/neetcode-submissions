class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        totals = {}

        for i, num in enumerate(nums):
            diff = target-num
            if diff in totals and totals[diff] != i:
                answer = [totals[diff], i]
                return sorted(answer)
            totals[num] = i

            