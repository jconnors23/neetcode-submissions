# Wrestle
# how do we handle sublist placement? - if act is placed in sublist - do we remove it from the orig
# i.e. if seen remove from arr before continue
# e.g. act goes in sublist 1, check and place matches, then - > actually just go L - > R, place as we go, everything will be seen at least once and placed in sublist group
# if seen create dict of word pairing - > then if matching previous pairing append to that sublist 
# for entry in sublist arr if entry of sublist of arr equals curr dict append word to that sublist 

# First

# init hash map
# sort each string alphabetically
# if sort in hm append word to seen hm key val list
# else init key val for sorted word
# at end - return all sublists lists in hm 

# Syntax 
# sort = "".join(sorted(curr))
# seen[sort] = [curr]
# return list(seen.values())
# collections.defaultdict(list)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            curr = strs[i]
            sort = "".join(sorted(curr)) #transform
            if sort in seen:
                seen[sort].append(curr) # organize
            else:
                seen[sort] = [curr]
        return list(seen.values()) # extract