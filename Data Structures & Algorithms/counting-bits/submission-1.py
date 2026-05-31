class Solution:
    def countBits(self, n: int) -> List[int]:

        answer = []
        for i in range(n+1):
            answer.append(self.count1s(i))

        return answer        



    def count1s(self, n: int):
        answer = 0
        while n > 0:
            if n % 2 == 1:
                answer += 1
            n = n >> 1
        return answer