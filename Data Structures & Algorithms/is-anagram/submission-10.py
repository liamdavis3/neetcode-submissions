class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s.lower()
        t.lower()
        for letter in s:
            if letter in t:
                t = t.replace(letter, "", 1)
            else:
                return False
        return len(t) == 0