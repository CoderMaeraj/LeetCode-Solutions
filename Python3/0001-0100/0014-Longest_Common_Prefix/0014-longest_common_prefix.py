from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def CommonPrefix(s1,s2):
            if s1 == s2:
                return s1
            comm = ""
            (a,b,i) = (len(s1),len(s2),0)
            while(i < min(a,b)):
                if s1[i] == s2[i]:
                    comm += s1[i]
                    i += 1
                else:
                    break
            return comm

        n = len(strs)
        comm_string = strs[0]
        for i in range(n):
            if comm_string == "":
                return comm_string
            comm_string = CommonPrefix(comm_string,strs[i])
        return comm_string