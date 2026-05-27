class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagrams = {}
        for word1 in strs:
            hit = False
            for word2 in anagrams:
                if self.check_anagrams(word1, word2) and not hit:
                    anagrams[word2] += [word1]
                    hit = True
            if not hit:
                anagrams[word1] = []
        for key in anagrams:
            answer = [key] + anagrams[key]
            output += [answer]
        print(output)
        return output

    def check_anagrams(self, word1: str, word2: str) -> bool:
        check = word2
        for letter in word1:
            if letter in check:
                check = check.replace(letter, "", 1)
            else:
                return False
        return len(check) == 0 and len(word1) == len(word2)