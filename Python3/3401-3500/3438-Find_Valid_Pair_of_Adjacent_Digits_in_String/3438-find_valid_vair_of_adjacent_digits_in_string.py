class Solution:
    def findValidPair(self, s: str) -> str:
        num_freq = {}
        for num in s:
            num_freq[num] = num_freq.get(num,0) + 1
        
        for i in range(len(s)-1):
            if (s[i] != s[i+1]) and ((int(s[i]) == num_freq[s[i]]) and (int(s[i+1]) == num_freq[s[i+1]])):
                return str(s[i]) + str(s[i+1])
        return ""
            