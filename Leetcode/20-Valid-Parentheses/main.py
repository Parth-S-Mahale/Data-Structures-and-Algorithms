class Solution(object):
    def isValid(self, s):
        mapping = {"(": ")", "[": "]", "{": "}"}
        stack= []
        
        for char in s:
            if char in '({[':
                stack.append(char)
            elif stack and char == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        