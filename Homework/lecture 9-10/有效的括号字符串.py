class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['?']
        pairs = {"(":")","[":"]","{":"}","?":"?"}
        if len(s)%2 == 1:
            return False
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif ch != pairs[stack.pop()]:
                return False
        if len(stack) == 1:
            return True
        else:
            return False