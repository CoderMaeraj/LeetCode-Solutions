class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashi = {}
        i=0
        prev_len = 0
        curr_len = 0
        while(i<n):
            if hashi.get(s[i],(0,0))[0] == 0:
                hashi[s[i]] = (1,i)
                curr_len += 1
                i+=1
            else:
                prev_len = max(prev_len, curr_len)
                curr_len = 0
                i = hashi[s[i]][1] + 1
                hashi.clear()
        return max(prev_len,curr_len)     

