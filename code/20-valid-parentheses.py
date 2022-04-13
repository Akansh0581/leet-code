# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        stack,par=[],{"{":"}","[":"]","(":")"}
        try:
            for c in s:
                if c in par.keys():
                    stack.append(c)
                if c in par.values():
                    if c != par[stack.pop()]:
                        return False
        except:
            return False
        return True if len(stack)==0 else False