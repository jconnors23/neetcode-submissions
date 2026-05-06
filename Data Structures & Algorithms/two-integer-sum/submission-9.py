# subtract index from tar, if tar minus next index = 0 return indices


# V1: list lookup
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             rest = nums[i+1:] # slice for rest of nums, ignoring i and detecting if target exists
#             if diff in rest:
#                 j = rest.index(diff) # find val at index 
#                 vals = [i, j+i+1] # relative positioning | i maps index from rest back to nums arr, +1 skips curr element so that i != j
#                 return vals
#         return None

# V2: map lookup
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         vals = dict()
#         for i in range(len(nums)):
#             vals[i] = nums[i] # val { 0: 3}
#             diff = target - vals[i]
#             for k, v in vals.items():
#                 if v == diff and k != i:
#                     return [k, i]


# V3: inverse map lookup 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {} # {val : index}
        for i, curr in enumerate(nums): # for k, v in arr
            diff = target - curr
            if diff in past: # if diff is in map struct two sum found
                return [past[diff], i] # seen[diff] = index, i equals present index
            past[curr] = i # add val : index to map
