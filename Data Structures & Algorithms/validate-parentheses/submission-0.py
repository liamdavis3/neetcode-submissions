class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        answers = set(["[]", "{}", "()"])

        for bracket in s:
            if len(stack) >= 1:
                value = stack.pop()
                print(value, bracket)
                if value+bracket not in answers:
                    stack.append(value)
                    stack.append(bracket)
                    
            else:
                stack.append(bracket)
        
        return len(stack) == 0
            
            