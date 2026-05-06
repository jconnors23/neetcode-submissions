# subtract index from tar, if tar minus next index = 0 return indices



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            rest = nums[i+1:] # slice for rest of nums, ignoring i and detecting if target exists
            if diff in rest:
                j = rest.index(diff) # find val at index 
                vals = [i, j+i+1] # relative positioning | i maps index from rest back to nums arr, +1 skips curr element so that i != j
                return vals
        return None
