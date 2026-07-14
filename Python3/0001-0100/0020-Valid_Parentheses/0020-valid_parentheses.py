class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapi = { "(" : ")", "{" : "}", "[" : "]" }
        openings = ["(", "{", "["]
        closings = [")", "}", "]"]

        for st in s:
            if st in openings:
                stack.append(mapi[st])
            if st in closings:
                if stack == []:
                    return False
                if stack.pop() != st:
                    return False
        
        if stack == []:
            return True
        else:
            return False