class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check = ""

        for letter in s:
            if letter.isalpha() or letter.isdigit():
                check+=letter.lower()
        print(check)


        return check == check[::-1]