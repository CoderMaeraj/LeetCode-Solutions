class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        res = 0
        neg = False
        dig_seen = False
        sig_seen = False
        space_end = False
        upper = (2**31) - 1
        lower = -2**31
        while(i<n):
            if s[i] == " ":
                if space_end:
                    break
                if dig_seen:
                    break
                i += 1
            elif s[i] == "-":
                if not(space_end):
                    space_end = True
                if dig_seen:
                    break
                if not(sig_seen):
                    sig_seen = True
                    neg = True
                    i += 1
                else:
                    break
            elif s[i] == "+":
                if not(space_end):
                    space_end = True
                if dig_seen:
                    break
                if not(sig_seen):
                    sig_seen = True
                    i += 1
                else:
                    break
            elif s[i].isdigit():
                if not(space_end):
                    space_end = True
                if not(dig_seen):
                    dig_seen = True
                res = res*10 + int(s[i])
                i += 1
            elif s[i].isalpha():
                break
            else:
                break
        if neg:
            res = -1*res
        if res > upper:
            return upper
        elif res < lower:
            return lower
        else:
            return res
        
            