class Solution:
    def romanToInt(self, s: str) -> int:
        symb_hash = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        prev = ""
        ans = 0
        for symb in s:
            if prev:
                if symb_hash[prev] >= symb_hash[symb]:
                    ans += symb_hash[symb]
                else:
                    ans = ans - 2*symb_hash[prev] + symb_hash[symb]
            else:
                ans += symb_hash[symb]
            prev = symb
        return ans