# subtract index from tar, if tar minus next index = 0 return indices



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            rest = nums[i+1:]
            if diff in rest:
                j = rest.index(diff)
                # if i == j: j+=1
                vals = [i, j+i+1]
                return vals
        return None
