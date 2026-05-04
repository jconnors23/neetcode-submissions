# create maps for s & t then check if s == t at end 


# V1 Compare two registries
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t): return False
#         sm, st = dict(), dict()
#         for i in range(len(s)):
#             curr = s[i]
#             if curr in sm:
#                 sm[curr]+=1
#             else:
#                 sm[curr] = 1
#             curr2 = t[i]
#             if curr2 in st:
#                 st[curr2]+=1
#             else:
#                 st[curr2] = 1
#         for k, v in sm.items():
#             if k not in st:
#                 return False
#             if v != st[k]:
#                 return False
#         return True 

# V2 - Single Registry

class Solution:
    import collections # remove key errors
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        comp = defaultdict(int)
        for i in range(len(s)):
            schar, tchar = s[i], t[i] # curr chars in both strs
            comp[schar] += 1
            comp[tchar] -= 1
        for v in comp.values():
            if v != 0: return False # any remaining chars removes equivalency
        return True
            
        