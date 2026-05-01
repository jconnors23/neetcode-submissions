# PC
# create dict keys are values in arr and values are count of num in arr

# return no val of 2 in dict?

# have if check at each pos in arr, if nums[i] in dict dict[nums[i]] ++ else dict[nums[[i] = 1

# at end go with return val of >=2 in dict 



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nd = dict()
        for i in range(len(nums)):
            curr = nums[i]
            if curr in nd:
                nd[curr]+=1
            else: 
                nd[curr]=1
        for k, v in nd.items():
            if v >= 2:
                return True
        return False

        