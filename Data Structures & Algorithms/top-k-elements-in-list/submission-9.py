class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        maxes = [0] * k

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)
        freq = dict(freq)
        freq = list(freq)
        
        for i in range(k):
            maxes[i] = freq[i]
        return maxes