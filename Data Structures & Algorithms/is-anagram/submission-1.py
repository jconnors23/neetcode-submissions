# create maps for s & t then check if s == t at end 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sm, st = dict(), dict()
        for i in range(len(s)):
            curr = s[i]
            if curr in sm:
                sm[curr]+=1
            else:
                sm[curr] = 1
            curr2 = t[i]
            if curr2 in st:
                st[curr2]+=1
            else:
                st[curr2] = 1
        for k, v in sm.items():
            if k not in st:
                return False
            if v != st[k]:
                return False
        return True 
            
        