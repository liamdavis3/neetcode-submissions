class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        maxes = [0] * k

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        print(freq)

        freq = sorted(freq.items(), key=lambda item: item[1], reverse = True)
        freq = dict(freq)
        print(freq)
        for i in range(k):
            maxes[i] = list(freq)[i]
        return maxes