import string
def Transform(s,k):
    n = len(s)
    if k == 0 or n==1:
        return int(s)
    else:
        ans = 0
        for i in range(n):
            ans += int(s[i])
        return Transform(str(ans),k-1)
    
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha = string.ascii_lowercase
        num_s = ''
        for i in range(len(s)):
            num_s += str((alpha.index(s[i])%26)+1)
        return Transform(num_s, k)