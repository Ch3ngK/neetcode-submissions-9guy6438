class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s) 
        for i in range(length):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if (bracket == '(' and s[i] != ')'):
                    return False
                if (bracket == '{' and s[i] != '}'):
                    return False
                if (bracket == '[' and s[i] != ']'):
                    return False
        return len(stack) == 0
            

